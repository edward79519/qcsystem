$(document).ready(function() {
    // {# 裡面所有的key都可以寫成字串 #}
    // ajax 改變鄉鎮市區的選項
    /*
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
    */
    // 抓 django form 產生的 id_county 值回傳給 id_area 的 option
    $(document).on('change', '#id_county', function () {
        var id_county = $('#id_county :selected').val();
        $.ajax({
            url: '/core/ajax/getarea/',
            method: "GET",
            data: {
                county: id_county
            },
            success: function (res) {
                $('#id_area').html(res);
                $('#id_section').html("");
                $('#county_ch').val($('#id_county :selected').text());
            },
        });
    });

    /*
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
                $('#id_section').html(res);
                $('#area_ch').val($('#area :selected').text());
            },
        });
    });
    */
    //
    $(document).on('change', '#id_area', function () {
        var area = $('#id_area :selected').val();
        var county = $('#id_county :selected').val();
        $.ajax({
            url: '/core/ajax/getsection/',
            method: "GET",
            data: {
                county: county,
                area: area,
            },
            success: function (res) {
                $('#id_section').html(res);
                $('#area_ch').val($('#id_area :selected').text());
            },
        });
    });

    /*
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
                    $('#cy').val("");
                    $('#cx').val("");
                    $('#id_cy').val("");
                    $('#id_cx').val("");
                }
                else {
                    $('#gpsmsg').text("");
                    $('#cy').val(res.gpsres.cy);
                    $('#cx').val(res.gpsres.cx);
                    $('#id_cy').val(res.gpsres.cy);
                    $('#id_cx').val(res.gpsres.cx);
                }
            },
        });
    });
    */

    $(document).on('click', '#id_findgps', function () {
        var office = $('#id_section :selected').attr('office');
        var section = $('#id_section :selected').attr('value');
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
                $('#id_office').val(res.office);
                $('#section_ch').val($('#id_section :selected').text());
                // $('#section').val(res.section);
                $('#id_locnum').val(res.locnum);
                if ( res.is_valid == 0 ) {
                    $('#gpsmsg').text(res.gpsres.msg);
                    $('#id_cy').val("");
                    $('#id_cx').val("");
                }
                else {
                    $('#gpsmsg').text("");
                    $('#id_cy').val(res.gpsres.cy);
                    $('#id_cx').val(res.gpsres.cx);
                    $('#id_ly').val(res.gpsres.ly);
                    $('#id_lx').val(res.gpsres.lx);
                    $('#id_ry').val(res.gpsres.ry);
                    $('#id_rx').val(res.gpsres.rx);
                }
            },
        });
    });


});

