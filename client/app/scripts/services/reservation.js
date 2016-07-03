'use strict';

/**
 * @ngdoc service
 * @name clientApp.Reservation
 * @description
 * # Reservation
 * Service in the clientApp.
 */
angular.module('clientApp')
.factory('Reservation', function ($localStorage) {
  if (!$localStorage.reservations) {
    $localStorage.reservations = [];
  }

  return {
    save: function(data) {
      $localStorage.reservations.push(data);
    },

    all: function() {
      return $localStorage.reservations;
    }
  };
});
