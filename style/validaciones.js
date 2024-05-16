$(document).ready(function() {
    // Inicializar Parsley en el formulario
    $('#registroForm').parsley();

    // Manejar errores de Parsley
    $('#registroForm').on('parsley:field:error', function() {
        var messages = ParsleyUI.getErrorsMessages($('#registroForm').parsley());
        var errorContainer = $('#errors-container');
        errorContainer.empty();
        $.each(messages, function(i, message) {
            errorContainer.append('<p>' + message + '</p>');
        });
    });

    // Limpiar mensajes de error cuando el campo es válido
    $('#registroForm').on('parsley:field:success', function() {
        $('#errors-container').empty();
    });
});
