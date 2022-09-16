# l10n_tool
Scripts to help make machine translate data of local files.

<pre>
A lot of small files to translate.
Translated data must in extract same line number.
Some source data is empty in a line.
Translate tool may broken the data order and the new line mark(CR/LF).

filename line_number ---data
a01.txt 1 ---dog
a01.txt 2 ---cat
a01.txt 3 ---snake
a02.txt 1 ---tiger
a02.txt 2 ---hawk
a03.txt 2 ---lion
a05.txt 8 ---chicken
</pre>
<pre>
8th 01mkold.8th
8th 02form.8th > all.out
rem Translate all.out data file to data.text with translate tool.
8th 03mknew.8th data.text
8th 04copy.8th
</pre>
