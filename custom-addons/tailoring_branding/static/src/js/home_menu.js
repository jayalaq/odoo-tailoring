/** @odoo-module **/

import { Component, useState, useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class HomeMenu extends Component {
    static template = "tailoring_branding.HomeMenu";
    static props = {
        onAppSelected: { type: Function, optional: true },
    };

    setup() {
        this.menuService = useService("menu");
        this.state = useState({ searchQuery: "" });
        this.searchInput = useRef("searchInput");

        onMounted(() => {
            if (this.searchInput.el) {
                this.searchInput.el.focus();
            }
        });
    }

    get apps() {
        return this.menuService.getApps();
    }

    get filteredApps() {
        const query = this.state.searchQuery.toLowerCase().trim();
        if (!query) {
            return this.apps;
        }
        return this.apps.filter((app) =>
            app.name.toLowerCase().includes(query)
        );
    }

    onSearchInput(ev) {
        this.state.searchQuery = ev.target.value;
    }

    selectApp(app) {
        this.menuService.selectMenu(app);
        if (this.props.onAppSelected) {
            this.props.onAppSelected();
        }
    }

    getMenuItemHref(payload) {
        return `/odoo/${payload.actionPath || "action-" + payload.actionID}`;
    }
}
