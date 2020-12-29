$(document).ready( function () {
    var tmp = `
            <tr>
                <td>
                    <div class="uk-form-controls">
                        <select class="uk-select">
                            <option>Option 01</option>
                            <option>Option 02</option>
                        </select>
                    </div>
                </td>
                <td>
                    <div class="uk-form-controls">
                        <input type="number" class="uk-input"  required name="watt" min="0" value="0" step=".01"  placeholder="what used">
                    </div>
                </td>
                <td>
                    <div class="uk-form-controls">
                        <input type="number" class="uk-input"  required name="huor" min="0" value="0" step=".01"  placeholder="what used">
                    </div>
                </td>
                <td>
                    <div class="uk-form-controls">
                        <input class="uk-input uk-form-width-medium" type="text" placeholder="disabled" value="10 W" disabled>
                    </div>
                </td>
            </tr>
    `
    $('#add-device').on( 'click', e => {
        $("tbody").append(tmp);
    });

    //$("tbody td").on('keyup', "input[name='huor']", function(e) {
    //    console.log($(this).val());
    //});

})