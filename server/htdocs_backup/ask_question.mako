<%inherit file="root.mako" />

<div class="header">
    <h1>${title}</h1>
</div>
<div class="registration_form" class="block">
    <form method="post" class="login form">
        <table>
            <tr>
                <td>${question}${question_str}</td>
            </tr>
            <tr>
                <td><input type="text" name="question_ans"/></td>
            </tr>
            <tr>
                </td>
                <td><input type="submit" name="form.commit"
                        value="${submit_text}"/></td>
            </tr>
        </table>
    </form>
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>
