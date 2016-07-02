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
    controller: 'ReserveCtrl as ctrl',
    resolve: {
      venue: function($stateParams, Venue) {
        return Venue.get({id: $stateParams.id});
      }
    }
  });

})
.controller('ReserveCtrl', function ($window, venue) {
  this.minDate = $window.moment();

  this.venue = venue;
});
