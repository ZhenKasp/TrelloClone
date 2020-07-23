        function getCookie(c_name)
    {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
     }

     $("#change-list-name").change(function (e) {
         e.preventDefault();        // preventing from page reload and default actions
         var serializedData = $("#name_1").serialize();      // serialize the data for sending the form data.

         $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
         });

         $.ajax({
             type: 'POST',
             url: "",
             data: serializedData,
         })
     })

    $("#change-list-name").change(function(e) {
        e.preventDefault();
        var str = $("#name_1").val();
        $("#list_1").text(str);
    });