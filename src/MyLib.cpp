#include "mylib/MyLib.h"
#include <iostream>

//libxml2 - just for showcase
#include <stdio.h>
#include <string.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <libxml/xmlIO.h>

namespace {
   const char* include = "<?xml version='1.0'?>\n\
<document>\n\
  <p>Hello world from libxml2!</p>\n\
</document>\n";
}

bool mylib::helloWorld(bool printXmlDoc) {
   if (printXmlDoc) {
      //Modified example from: http://xmlsoft.org/examples/io1.c
      xmlDocPtr doc;

      /*
       * this initialize the library and check potential ABI mismatches
       * between the version it was compiled for and the actual shared
       * library used.
       */
      LIBXML_TEST_VERSION

         /*
          * parse include into a document
          */
         doc = xmlReadMemory(include, strlen(include), "include.xml", NULL, 0);
      if (doc == NULL) {
         fprintf(stderr, "failed to parse the including file\n");
         exit(1);
      }


#ifdef LIBXML_OUTPUT_ENABLED
      /*
       * save the output for checking to stdout
       */
      xmlDocDump(stdout, doc);
#endif

      /*
       * Free the document
       */
      xmlFreeDoc(doc);

      /*
       * Cleanup function for the XML library.
       */
      xmlCleanupParser();
      /*
       * this is to debug memory for regression tests
       */
      xmlMemoryDump();
   }
   else {
      std::cout << "Hello world!\n";
   }
   return printXmlDoc;
}
