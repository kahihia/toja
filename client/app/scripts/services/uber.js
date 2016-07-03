'use strict';

/**
 * @ngdoc service
 * @name clientApp.Uber
 * @description
 * # Uber
 * Service in the clientApp.
 */
angular.module('clientApp')
  .factory('Uber', function () {
    var uberClientId = 'zHB8o86RL50750GPHNh_TkQfonFR0he3';

    return {
      /**
       * Generate universal ride request URL
       * @param  {Object} params
       * @param  {Object} params.dropoff - drop off location
       * @param  {String} params.dropoff.latitude - drop-off location lat
       * @param  {String} params.dropoff.longitude - drop-off location long
       * @param  {String} params.dropoff.name - name of the drop-off location
       * @param  {Object} params.pickup - pickup location
       * @param  {String} params.pickup.latitude - pickup location lat
       * @param  {String} params.pickup.longitude - pickup location long
       * @param  {String} params.pickup.name - name of the pickup location
       * @return {[type]}        [description]
       */
      generateRideRequestUrl: function(params) {
        var uberURL = 'uber://?';
        uberURL += 'client_id=' + uberClientId + '&action=setPickup';

        if (params.pickup) {
          uberURL += '&pickup[nickname]=' + params.pickup.name;
          uberURL += '&pickup[latitude]=' + params.pickup.latitude;
          uberURL += '&pickup[longitude]=' + params.pickup.longitude;
        }

        if (params.dropoff) {
          uberURL += '&dropoff[nickname]=' + params.dropoff.name;
          uberURL += '&dropoff[latitude]=' + params.dropoff.latitude;
          uberURL += '&dropoff[longitude]=' + params.dropoff.longitude;
        }

        return uberURL;
      }
    };
  });
