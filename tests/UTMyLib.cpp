#include "mylib/MyLib.h"
#include <gtest/gtest.h>

TEST(MyLib, printCout)
{
   ASSERT_FALSE(mylib::helloWorld(false));
}

TEST(MyLib, printXmlDoc)
{
   ASSERT_TRUE(mylib::helloWorld(true));
}