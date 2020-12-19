function sendValues(){
            var name_1 = document.getElementById("name_1").value;
            var name_2 = document.getElementById("name_2").value;
            var tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
            $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({'user_1': name_1, 'user_2': name_2, 'time_zone': tz}),
                dataType: 'json',
                url: 'http://127.0.0.1:5000/results'
            });

            location.href = 'http://127.0.0.1:5000/statistics'
        }