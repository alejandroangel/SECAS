<%inherit file="root.mako" />

<div class="col-md-4 col-md-offset-4 header">
    <h1>${title}</h1>
</div>
<div class="col-md-4 col-md-offset-4 registration_form login_form" class="block">
    <form method="post" class="login form">
        <table>
            <tr>
                <td>${username_title}</td>
                <td><input class="form-control" type="text" name="username"/></td>
            </tr>
        </table>
        <div><input class="form-control" type="hidden" name="url" value="${url}"/></div>
        <div><input class="btn btn-primary btn-lg btn-block" type="submit" name="form.commit"
                        value="${submit_text}"/></div>

    </form>
    <a href="${url}"><strong>BACK</strong></a><br>
</div>

<%def name="add_js()">
    <script type="text/javascript">
        $(document).ready(function() {
            bookie.login.init();
        });
    </script>
</%def>