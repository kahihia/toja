'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:ReserveCtrl
 * @description
 * # ReserveCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('reserve', {
    url: '/reserve/:id',
    templateUrl: 'views/reserve.html',
    controller: 'ReserveCtrl as ctrl'
  });

})
.controller('ReserveCtrl', function ($window) {
  this.minDate = $window.moment();
});
