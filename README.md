# appy-test

Some test about Appy Framework [http://appyframework.org/]

With Appy you can create reports and documents starting from LibreOffice odt file as template.

1. write an ODT file with some fields and notes (see Appy documentation)

2. write a python script to validate the fileds and generate the output document





PDF Generation
--------------

In order to generate PDF document, Appy needs to connect to a running libreoffice instance, started as server (headless).

You can use this command:
<code>libreoffice5.0 --invisible --headless --nofirststartwizard "--accept=socket,host=localhost,port=2002;urp;"</code>

And you have to set the python interpreter installed with libreoffice, when calling the Renderer (see the python script)





