'use strict';

/**
 * @ngdoc overview
 * @name clientApp
 * @description
 * # clientApp
 *
 * Main module of the application.
 */
angular
.module('clientApp', [
  'ngAnimate',
  'ngAria',
  'ngCookies',
  'ngMessages',
  'ngResource',
  'ngRoute',
  'ngSanitize',
  'ngTouch',
  'ngMaterial',
  'ui.router',
  'ksSwiper',
  'uiGmapgoogle-maps'
])
.config(function ($urlRouterProvider, uiGmapGoogleMapApiProvider) {
  $urlRouterProvider.otherwise('/');

  uiGmapGoogleMapApiProvider.configure({
    key: 'AIzaSyBwhccxQP4Au0m2QgiGXbqMEDr54728uTo',
    v: '3.20', //defaults to latest 3.X anyhow
    libraries: 'weather,geometry,visualization'
  });
})
.run(function($rootScope, $window, $state) {
  $rootScope.navigateBack = function() {
    $window.history.back();
  };

  $rootScope.navigateTo = function(state, params) {
    $state.go(state, params);
  };
});
