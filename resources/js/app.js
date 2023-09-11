import './bootstrap'

import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/vue3';
import {ZiggyVue} from "ziggy-js/dist/vue.m";
import { modal } from "momentum-modal";
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import ConfirmationService from 'primevue/confirmationservice';


createInertiaApp({
    resolve: (name) => require(`./pages/${name}`),
    setup({el, App, props, plugin}) {
        return createApp({
            render: () => h(App, props)
        })
        .mixin({
            methods: {
                route(name, params = {}, absolute = true) {
                    return route(name, params, absolute, window.Ziggy);
                },
            },
        })
        .use(modal, {
            resolve: (name) => require(`./modals/${name}`),
        })
        .use(PrimeVue)
        .use(ToastService)
        .use(ConfirmationService)
        .use(plugin)
        .use(ZiggyVue, Ziggy)
        .mount(el);
     },
    progress: {
        color: '#4B5563',
    },
}).then(r =>console.log(r));
