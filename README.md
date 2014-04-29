# CybOX Document Validator (cdv)
A python tool used to validate CybOX v2.1 instance documents. For more information about the
Cyber Observable eXpression, see http://cybox.mitre.org.

## Dependencies
The CybOX Document Validator has the following dependencies:
* Python v2.7 http://python.org/download
* lxml >= v3.2.0 http://lxml.de/index.html#download
  * libxml2 >= v2.9.1 http://www.xmlsoft.org/downloads.html

For a Windows installer of lxml, we recommend looking here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml

## Common Libxml2 Error
Users often report an error which looks something like the following:
```
Fatal error occurred: local union type: A type, derived by list or union, must have the 
simple ur-type definition as base type, not '{http://cybox.mitre.org/common-2}(NULL)'., line 350
```
This error is caused by an insufficient version of libxml2 being installed on the system. The 
cybox-validator requires libxml2 v2.9.1 at a minimum and is not guaranteed to work properly with
earlier versions. 

To see what version of libxml2 you have installed, execute the `xml2-config --version` command
and make sure you are running at least v2.9.1.

## Use
The CybOX Document Validator can validate a CybOX v2.1 instance document against CybOX v2.1 schemas
found locally or referenced remotely through the schemaLocation attribute. 

**Validate using local schemas**  
`python cdv.py --input-file <cybox_document.xml> --schema-dir schema`

**Validate using schemaLocation**  
`python cdv.py --input-file <cybox_document.xml> --use-schemaloc`

**Validate a directory of CybOX documents**  
`python cdv.py --input-dir <cybox_dir> --schema-dir schema`

**Export JSON Results**  
`python cdv.py --input-dir <cybox_dir> --schema-dir schema --json-results`

## All CybOX Documents?
The CybOX Document Validator bundles a schema directory with it, which includes all CybOX v2.1 
schema files. If an instance document uses constructs or languages defined by other schemas
a user must point the CybOX Document Validator at those schemas in order to validate.

## Terms
BY USING THE CYBOX DOCUMENT VALIDATOR, YOU SIGNIFY YOUR ACCEPTANCE OF THE 
TERMS AND CONDITIONS OF USE.  IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE 
THE CybOX DOCUMENT VALIDATOR.

For more information, please refer to the LICENSE.txt file
