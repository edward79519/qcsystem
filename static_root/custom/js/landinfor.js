$(document).ready(function() {
    // {# 裡面所有的key都可以寫成字串 #}
    // ajax 改變鄉鎮市區的選項
    $(document).on('change', '#county', function () {
        var county = $('#county :selected').val();
        $.ajax({
            url: '/core/ajax/getarea/',
            method: "GET",
            data: {
                county: county
            },
            success: function (res) {
                $('#area').html(res);
                $('#county_ch').val($('#county :selected').text());
            },
        });
    });

    $(document).on('change', '#area', function () {
        var area = $('#area :selected').val();
        var county = $('#county :selected').val();
        $.ajax({
            url: '/core/ajax/getsection/',
            method: "GET",
            data: {
                county: county,
                area: area,
            },
            success: function (res) {
                $('#section').html(res);
                $('#area_ch').val($('#area :selected').text());
            },
        });
    });

    $(document).on('click', '#findgps', function () {
        var office = $('#section :selected').attr('office');
        var section = $('#section :selected').attr('value');
        var locnum1 = $('#locnum1').val();
        var locnum2 = $('#locnum2').val();

        $.ajax({
            url: '/core/ajax/getlandgps/',
            method: "GET",
            data: {
                office: office,
                section: section,
                locnum1: locnum1,
                locnum2: locnum2,
            },
            success: function (res) {
                $('#office_id').val(res.office);
                $('#section_ch').val($('#section :selected').text());
                $('#section').val(res.section);
                $('#locnum').val(res.locnum);
                if ( res.gpsres.msg=="地號查詢無資料!" ) {
                    $('#gpsmsg').text(res.gpsres.msg);
                }
                else {
                    $('#cy').val(res.gpsres.cy);
                    $('#cx').val(res.gpsres.cx);
                }
            },
        });
    });
});