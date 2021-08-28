require 'sinatra'
require 'sinatra/json'
set :port, 8888

get '/api/echo/:words' do
  # Log request
  # Automatically done

  # Parse parameters
  words = params['words']
  num = params['num']

  # Verify parameters
  if words.downcase != 'helloworld' || Integer(num) != 1234567890
    status 400 and json :error => 'Invalid parameters'
  else
    # Return response
    status 200 and json :message => SecureRandom.uuid
  end
end
