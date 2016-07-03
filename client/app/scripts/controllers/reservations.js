'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:ReservationsCtrl
 * @description
 * # ReservationsCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('reservations', {
    url: '/reservations',
    templateUrl: 'views/reservations.html',
    controller: 'ReservationsCtrl as ctrl'
  });

})
.controller('ReservationsCtrl', function ($rootScope, Reservation) {
  this.reservations = Reservation.all();

  $rootScope.navTitle = 'Revervation history';
});
