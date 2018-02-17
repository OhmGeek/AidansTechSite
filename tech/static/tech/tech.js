jQuery('document').ready(function() {
    $(".tag-list").each(function() {
        var importance = {
            power: 1,
            lighting: 2,
            sound: 3
        };
        var tagElems = $(this).children(".badge");
        var tagList = [];
        for (var i = 0; i < tagElems.length; i++) {
            tagList.push(tagElems[i]);
        }
        if (tagList.length) {
            tagList.sort(function(a, b) {
                var textA = a.textContent.trim().toLowerCase();
                var textB = b.textContent.trim().toLowerCase();
                if (importance.hasOwnProperty(textA) || importance.hasOwnProperty(textB)) {
                    a = importance[textA] || 0;
                    b = importance[textB] || 0;
                    return b - a;
                } else {
                    return textB < textA;
                }
            });
            $(this).empty();
            for (var i = 0; i < tagList.length; i++) {
                $(this).append(tagList[i]);
            }
        }
    });

    $(".js-example-basic-multiple").select2();

    var $grid = $('.grid');
    $grid.isotope({
        itemSelector: '.grid-item',
        layoutMode: 'packery',
        packery: {
            gutter: 4
        },
        fitWidth: true,
        percentPosition: true,
    });
    $('#filter-options').on('change', function() {
        var names = this.selectedOptions
        names = [].slice.call(names); //convert to array
        if(names) {
            var stringClasses = "";
            names.forEach(function(elem, index) {
                stringClasses += "." + elem.innerText;
            });
            $grid.isotope({filter: stringClasses});
        } else {
            $grid.isotope({
                filter: "*"
            });
        }
    });
});
