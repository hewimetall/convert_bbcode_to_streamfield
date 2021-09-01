from bbcode import Parser
import re

class OneLevel(Parser):

    def install_default_formatters(self):
        """
        Installs default formatters for the following tags:

            b, i, u, s, list (and *), quote, code
        """
        self.add_simple_formatter("b", "<strong>%(value)s</strong>")
        self.add_simple_formatter("i", "<em>%(value)s</em>")
        self.add_simple_formatter("u", "<u>%(value)s</u>")
        self.add_simple_formatter("s", "<strike>%(value)s</strike>")
        self.add_simple_formatter("small", "<small>%(value)s</small>")
        self.add_simple_formatter("nbsp", "&nbsp", standalone=True)
        self.add_simple_formatter("sub", "<sub>%(value)s</sub>")
        self.add_simple_formatter("sup", "<sup>%(value)s</sup>")

        def _render_list(name, value, options, parent, context):
            list_type = options["list"] if (options and "list" in options) else "*"
            css_opts = {
                "1": "decimal",
                "01": "decimal-leading-zero",
                "a": "lower-alpha",
                "A": "upper-alpha",
                "i": "lower-roman",
                "I": "upper-roman",
            }
            tag = "ol" if list_type in css_opts else "ul"
            css = ' style="list-style-type:%s;"' % css_opts[list_type] if list_type in css_opts else ""
            return "<%s%s>%s</%s>" % (tag, css, value, tag)

        self.add_formatter("list", _render_list, transform_newlines=False, strip=True, swallow_trailing_newline=True)
        def _render_list_item(name, value, options, parent, context):
            if not parent or parent.tag_name != "list":
                return "[*]%s<br />" % value

            return "<li>%s</li>" % value

        self.add_formatter(
            "*", _render_list_item, newline_closes=True, transform_newlines=False, same_tag_closes=True, strip=True
        )
        self.add_formatter("list", _render_list, transform_newlines=False, strip=True, swallow_trailing_newline=True)
        #self.add_formatter("url", self.url, replace_links=False, replace_cosmetic=False)

        def _render_url(name, value, options, parent, context):
            if len(options):
                href = list(options.keys())[0]
                # Option values are not escaped for HTML output.
                href = self._replace(href, self.REPLACE_ESCAPE)
            else:
                href = value
            # Completely ignore javascript: and data: "links".
            if re.sub(r"[^a-z0-9+]", "", href.lower().split(":", 1)[0]) in ("javascript", "data", "vbscript"):
                return ""
            # Only add the missing http:// if it looks like it starts with a domain name.
            if "://" not in href:
                href = "http://" + href
            return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (href , value)

        self.add_formatter("url", _render_url, replace_links=False, replace_cosmetic=False)
        self.add_formatter('email',self.email)

    def email(self, name, value, options, parent, context):
        """BB код [email]"""
        if len(options):
            href = list(options.keys())[0]
        else:
            href = value
        return u'<a href="mailto:%s">%s</a>' % (href, value)
