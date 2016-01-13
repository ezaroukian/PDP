define_ibex_controller({
    name: "ClickSeparator",
    jqueryWidget: {
        _init: function () {
            this.element.VBox({
                options: this.options,
                triggers: [1],
                children: [
                    "SeparatorHTML", this.options,
                    "Message", this.options ]
            });
        }
    },
    properties: {
	}
});