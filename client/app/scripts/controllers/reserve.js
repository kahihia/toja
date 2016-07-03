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
.controller('ReserveCtrl', function (
  $rootScope, $window, $stateParams, $localStorage, $state, Reservation, venue
) {
  var venueId, self = this;

  $rootScope.navTitle = 'Make reservation';

  this.minDate = $window.moment();

  this.reservationDate = null;
  this.reservationTime = null;

  this.reservation = {
    name: '',
    npeople: 2,
    datetime: null,
    resid: $stateParams.id,
    cusphone: '',
    lang: 'ja'
  };

  this.venue = venue;
  this.venue.$promise.then(function() {
    venueId = self.venue.id;
  });

  this.reserve = function() {
    this.reservationDate.setHours(this.reservationTime.getHours());
    this.reservationDate.setMinutes(this.reservationTime.getMinutes());
    this.reservation.datetime = this.reservationDate.getTime() / 1000;

    console.debug('Making reservation for venue', this.venue);
    this.venue.$reserve(this.reservation).then(function(data) {
      console.debug('Reservation has been made', data);
      var call = data;
      call.venueId = venueId;

      Reservation.save(call);
      $state.go('reservations');
    }).catch(function(error) {
      console.debug('Cannot make the reservation', error);
    });
  };
});
