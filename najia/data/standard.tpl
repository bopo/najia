{{gender}}测：{{title}}

公历：{{solar.year}}年 {{solar.month}}月 {{solar.day}}日 {{solar.hour}}时 {{solar.minute}}分
干支：{{lunar.gz.year}}年 {{lunar.gz.month}}月 {{lunar.gz.day}}日 {{lunar.gz.hour}}时 （旬空：{{lunar.xkong}})

得「{{name}}」{% if bian.name %}之「{{bian.name}}」{% endif %}卦

{{main.indent}}{{main.gong}}宫:{{main.name}}{% if main.type %} ({{main.type}}){% endif %}{{bian.indent}}{% if bian.name %}{{bian.gong}}宫:{{bian.name}}{% if bian.type %} ({{bian.type}}){% endif %}{% endif %}
{{god6.5}}{{hide.qin6.5}}{{qin6.5}}{{qinx.5}} {{main.mark.5}} {{shiy.5}} {{dyao.5}} {{bian.qin6.5}} {{bian.mark.5}}
{{god6.4}}{{hide.qin6.4}}{{qin6.4}}{{qinx.4}} {{main.mark.4}} {{shiy.4}} {{dyao.4}} {{bian.qin6.4}} {{bian.mark.4}}
{{god6.3}}{{hide.qin6.3}}{{qin6.3}}{{qinx.3}} {{main.mark.3}} {{shiy.3}} {{dyao.3}} {{bian.qin6.3}} {{bian.mark.3}}
{{god6.2}}{{hide.qin6.2}}{{qin6.2}}{{qinx.2}} {{main.mark.2}} {{shiy.2}} {{dyao.2}} {{bian.qin6.2}} {{bian.mark.2}}
{{god6.1}}{{hide.qin6.1}}{{qin6.1}}{{qinx.1}} {{main.mark.1}} {{shiy.1}} {{dyao.1}} {{bian.qin6.1}} {{bian.mark.1}}
{{god6.0}}{{hide.qin6.0}}{{qin6.0}}{{qinx.0}} {{main.mark.0}} {{shiy.0}} {{dyao.0}} {{bian.qin6.0}} {{bian.mark.0}}

{% if guaci %}{{ guaci }}{% endif %}
