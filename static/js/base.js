const visibleForm = () => {
    if ($('.check-upload-file').get(0).files.length !== 0) {
        $('#form_invisible').css("visibility" , 'visible');
    }

}
const getResizeImage = () => {

    if ($('.resize-image').val() === '') {
        swal('Update the Image');
        return
    } else if ($('.image-width').val() === '') {
        swal('Add Resize Image Width');
        return;
    } else if ($('.image-height').val() === '') {
        swal('Add Resize Image Height');
        return;
    }

    var form_data = new FormData($('#upload-file')[0]);
    $.ajax({
        type: 'POST',
        url: '/resize-image',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            console.log(data);
            setTimeout(function () {
                $('#link').attr('href', data['url']);
                $('#count').text(data['count']);
                swal('Your Image is ready Please Download it using below button!')
            }, 3000);

        },
    });


}

$('#hw-checkbox').click(function(){
            if($(this).prop("checked") == true){
                $( ".enable-hw" ).prop( "disabled", false );
            }
            else if($(this).prop("checked") == false){
                $( ".enable-hw" ).prop( "disabled", true );
            }
        });
