# N21 Challenge question

We would like you to implement a Trie (see https://en.wikipedia.org/wiki/Trie) with the following data.
The idea is to build a data structure that makes it easy to find specific terms in some text.
Supposing I have a set of terms, I can put them in the data structure and run my text through the data structure to see which of those terms are in the text.

A term may be multiple words (sometimes we call those words tokens).  You should build the Trie using tokens (not characters - which is the most common explanation and is what is showing in wikipedia).

The terms to put in the Trie are these:

* Borrower
* Subsidiaries
* Material Project Party
* Project
* Project Manager
* Anti-Money Laundering Laws
* Sanctions
* Anti-Corruption Laws
* Affiliates
* Sanctioned Person
* Sanctioned Country
* Person
* Officer
* Director
* Agents


The text to then run through the trie to search for what terms are in the text follows below.
You'll need to "tokenize" the text at some point and probably clean off punctuation and so on.

What we'd like to see is the resulting code and the results of running this text through the Trie with the above terms.

TheText to process with the Trie:

The operations of each Borrower, and the activities of the officers and directors and, to the knowledge of each Borrower, 
any Subsidiaries of the Borrowers, employees, agents and representatives of each Borrower, while acting on behalf of such 
Borrower, and to the knowledge of each Borrower the operations of each Material Project Party in relation to the Project, 
have been conducted at all times in compliance with all applicable Anti-Money Laundering Laws, Sanctions, and Anti-Corruption 
Laws. Neither Borrower, nor any Subsidiaries of the Borrowers, nor any officer or director or, to the knowledge of any Borrower, 
Affiliates, employee, agent or representative of either Borrower has engaged, directly or indirectly, in any activity or conduct 
which would violate any Anti-Corruption Laws or Anti-Money Laundering Laws. Neither Borrower nor any Subsidiaries of the Borrowers, 
nor any officer or director or, to the knowledge of any Borrower, Affiliates, employee, agent or representative of either Borrower 
has engaged, directly or indirectly, in any dealings or transactions with, involving or for the benefit of a Sanctioned Person,
or in or involving a Sanctioned Country, where such dealings or transactions would violate Sanctions, in the five (5) year period
immediately preceding the date hereof.
