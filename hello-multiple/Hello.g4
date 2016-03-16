// Define a grammar called Hello
grammar Hello;            // defines how the output code will be named
prog : hi* EOF;           // accept zero or more hello items followed by EOF
hi : 'hello' ID ;         // match keyword hello followed by an identifier
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

