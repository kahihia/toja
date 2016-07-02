'use strict';

/**
 * @ngdoc service
 * @name clientApp.Venue
 * @description
 * # Venue
 * Service in the clientApp.
 */
angular.module('clientApp')
  .service('Venue', function ($resource, API_END_POINT) {
    return $resource(API_END_POINT + '/api/venues/:id', {}, {
      query: {
        method: 'GET',
        isArray: true
      }
    });
  });
