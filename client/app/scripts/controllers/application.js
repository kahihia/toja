'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:ApplicationCtrl
 * @description
 * # ApplicationCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
  .controller('ApplicationCtrl', function ($state) {
    this.$state = $state;
  });
