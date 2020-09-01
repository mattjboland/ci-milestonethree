$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
    $('.icon-rotate').click(function() {
        var down = $('.icon-rotate').hasClass("fa-caret-down");
        if(down){
            $('.icon-rotate').removeClass("fa-caret-down").addClass("fa-caret-right");
        }else{
            $('.icon-rotate').removeClass("fa-caret-right").addClass("fa-caret-down");
        }
    });
    
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

});

 var ingredientField = $(".ingredient").length;
    $("#add_ingredient").on("click", function () {
        $("select").formSelect("destroy");
        $(".new-ingredient:first").clone().insertBefore("#add_ingredient").find("input[type='text'], select, textarea").val("");
        $("select").formSelect();
        ingredientField += 1;
    });

    $("#remove_ingredient").on("click", function () {
        if (ingredientField > 1) {
            /* only remove the :last item */
            $(this).siblings(".new-ingredient:last").remove();
            /* ensure original ingredient line never gets deleted */
            ingredientField-= 1;
        }
    });

    var methodField = $(".method").length;
    /* add new cloned item */
    $("#add_step").on("click", function () {
        $(".new-step:first").clone().insertBefore("#add_step").find("input[type='text'], select, textarea").val("");
        /* increase counter so original direction is never removed */
       methodField += 1;
    });
    /* delete last cloned item */
    $("#remove_step").on("click", function () {
        if ( methodField > 1) {
            /* only remove the :last item */
            $(this).siblings(".new-step:last").remove();
            /* ensure original direction line never gets deleted */
            methodField-= 1;
        }
    });

        
