# Use the official Node.js image from the Docker Hub
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React application
RUN npm run build

# Install a simple server to serve the static files
RUN npm install -g serve

# Expose port 3000 for the frontend
EXPOSE 3000

# Start the React application
CMD ["serve", "-s", "build"]