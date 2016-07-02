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
        isArray: true,
        transformResponse: function(data) {
          var records = angular.fromJson(data);

          if (!records) {
            return [];
          }

          // TODO: return Array of images from server side
          // instead of String
          if (records instanceof Array) {
            records.map(function(record) {
              record.images = JSON.parse(record.images);
              return record;
            });
            return records;
          }
        }
      }
    });
  });
