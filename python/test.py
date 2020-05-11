test_string=u"环球老虎财经: 交通银行（601328.SH）混合所有制&#34;起底&#34; "



import lxml.html

x=lxml.html.fromstring(test_string)

print(x.text_content())
