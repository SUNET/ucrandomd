
import socket
import threading
import SocketServer
import getopt
import sys

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        with open(self.server.config.get('-d'),"rb") as fd:
            sz = int(self.server.config.get('-S'))
            print "reading %d bytes" % sz
            response = fd.read(sz)
            print "got %d bytes" % len(response)
            self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    main()

def usage():
    sys.exit(1)

def main():
    # Port 0 means to select an arbitrary unused port
    opts = {}
    args = []
    flags = "fhvd:p:H:S:"

    try:
        opts, args = getopt.getopt(sys.argv[1:], flags)
        opts = dict(opts)
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    if '-h' in opts:
        usage()
        sys.exit()

    if '-v' in opts:
        print "ucrandom version %s (c) SUNET 2016" % VERSION
        sys.exit()

    opts.setdefault('-p',4711)
    opts.setdefault('-H',"0.0.0.0")
    opts.setdefault('-d',"/dev/random")
    opts.setdefault('-L',"WARNING")
    opts.setdefault('-P',"/var/run/ucrandom.pid")
    opts.setdefault('-S',1024)

    server = ThreadedTCPServer((opts.get('-H'), int(opts.get('-p'))), ThreadedTCPRequestHandler)
    server.config = opts

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = '-f' not in opts
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    try:
       server.serve_forever()
    except KeyboardInterrupt:
       pass

    server.shutdown()
    server.server_close()
