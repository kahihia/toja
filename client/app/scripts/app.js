/* jshint ignore:start */
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
  'uiGmapgoogle-maps',
  'ngMaterialDatePicker',
  'ngStorage',
  'angular-inview',
  'geolocation'
])
.constant('API_END_POINT', 'http://10.201.120.132:8000')

.config(function ($urlRouterProvider, uiGmapGoogleMapApiProvider) {
  $urlRouterProvider.otherwise('/');

  uiGmapGoogleMapApiProvider.configure({
    v: '3.2', //defaults to latest 3.X anyhow
    libraries: 'weather,geometry,visualization'
  });
})
.run(function($rootScope, $window, $state, $timeout, $document) {
  $rootScope.navigateBack = function() {
    $window.history.back();
  };

  $rootScope.navigateTo = function(state, params) {
    $state.go(state, params);
  };

  $rootScope.showBusy = function() {
    console.debug('Showing busy');
    $rootScope.isLoading = true;
  };

  $rootScope.hideBusy = function() {
    console.debug('Hiding busy');
    $rootScope.isLoading = false;
  };

  $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
    if (toState.resolve) {
      $rootScope.showBusy();
    }
  });

  $rootScope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams) {
    if (toState.resolve) {
      $timeout(function() {
        $rootScope.hideBusy();
      });
    }
  });

  // Scroll to top after changing state
  function scrollToTop() {
    $timeout(function() {
      $document[0].scrollTop =  0;
    });
  }

  $rootScope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams) {
    scrollToTop();
  });
});
/* jshint ignore:end */
