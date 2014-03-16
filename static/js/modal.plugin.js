/**
 * Plugin created to invoke dialog modals to actions execution, how exclusion, etc.
 *
 * For instance:
 *
 *
 * <a href="#" data-url="{% url 'app:delete' 'obj.slug' %}">Delete</a>
 *
 * $('.linkDialog').deleteDialog();
 *
 */
(function($) {
    $.fn.deleteDialog = function() {
        $(this).on('click', function() {
            var $link = $(this);
            BootstrapDialog.show({
                title: 'Delete Item',
                message: 'Really delete this item?',
                buttons: [{
                    label: 'Yes',
                    cssClass: 'btn-success',
                    action: function(dialog) {
                        document.location = $link.attr('data-url');
                    }
                }, {
                    label: 'No',
                    action: function(dialog) {
                        dialog.close();
                    }
                }]
            });
        });
    };
})(jQuery);

