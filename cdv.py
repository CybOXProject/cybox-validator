#!/usr/bin/env python

# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
CybOX Document Validator (cdv) - validates CybOX v2.1 instance documents.
'''
import os
import argparse
import json
from validators import XmlValidator

__version__ = "2.1.0.0"
QUIET_OUTPUT = False

def get_files_to_validate(dir):
    '''Return a list of xml files under a directory'''
    to_validate = []
    for fn in os.listdir(dir):
        if fn.endswith('.xml'):
            fp = os.path.join(dir, fn)
            to_validate.append(fp)
            
    return to_validate

def error(msg):
    '''Print the error message and exit(1)'''
    print "[!] %s" % (msg)
    exit(1)

def info(msg):
    '''Prints an info message'''
    if QUIET_OUTPUT: 
        return
    print "[-] %s" % msg

def print_schema_results(fn, results):
    if results.get('result', False):
        print "[+] XML schema validation results: %s : VALID" % fn
    else:
        print "[!] XML schema validation results: %s : INVALID" % fn
        print "[!] Validation errors"
        for error in results.get("errors", []):
            print "    [!] %s" % (error)
 
def main():
    parser = argparse.ArgumentParser(description="CybOX 2.1 Document Validator")
    parser.add_argument("--schema-dir", dest="schema_dir", default=None, help="Path to directory containing all necessary schemas for validation")
    parser.add_argument("--input-file", dest="infile", default=None, help="Path to CybOX instance document to validate")
    parser.add_argument("--input-dir", dest="indir", default=None, help="Path to directory containing CybOX instance documents to validate")
    parser.add_argument("--use-schemaloc", dest="use_schemaloc", action='store_true', default=False, help="Use schemaLocation attribute to determine schema locations.")
    parser.add_argument("--quiet", dest="quiet", action="store_true", default=False, help="Only print results and errors if they occur")
    parser.add_argument("--json-results", dest="json", action="store_true", default=False, help="Print results as raw JSON. This also sets --quiet.")
    
    args = parser.parse_args()
    global QUIET_OUTPUT
    QUIET_OUTPUT = args.quiet or args.json
    schema_validation = False
    
    if (args.infile or args.indir) and (args.schema_dir or args.use_schemaloc):
        schema_validation = True
    if args.infile and args.indir:
        error('Must provide either --input-file or --input-dir argument, but not both')
    if args.schema_dir and args.use_schemaloc:
        error("Must provide either --use-schemaloc or --schema-dir, but not both")
    if (args.infile or args.indir) and not (args.schema_dir or args.use_schemaloc):
        error("Must provide either --use-schemaloc or --schema-dir when --input-file or input-dir declared")
         
    try: 
        if schema_validation:
            if args.infile:
                to_validate = [args.infile]
            elif args.indir:
                to_validate = get_files_to_validate(args.indir)
            else:
                to_validate = []
            
            if len(to_validate) > 0:
                info("Processing %s files" % (len(to_validate)))
                validator = XmlValidator(schema_dir=args.schema_dir, use_schemaloc=args.use_schemaloc)
                for fn in to_validate:
                    schema_results = {}
                    
                    info("Validating CybOX document %s against XML schema... " % fn)
                    schema_results = validator.validate(fn)
                    
                    if args.json:
                        json_results = {}
                        if schema_results:
                            json_results['schema_validation'] = schema_results
                        print json.dumps(json_results)
                    else:
                        if schema_results: 
                            print_schema_results(fn, schema_results)
                        
    except Exception as ex:
        error("Fatal error occurred: %s" % str(ex))
    
if __name__ == '__main__':
    main()

    