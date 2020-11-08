--- wifijammer	(original)
+++ wifijammer	(refactored)
@@ -111,7 +111,7 @@
         return monitors[0]
     else:
         # Start monitor mode on a wireless interface
-        print '['+G+'*'+W+'] Finding the most powerful interface...'
+        print('['+G+'*'+W+'] Finding the most powerful interface...')
         os.system('pkill NetworkManager')
         interface = get_iface(interfaces)
         monmode = start_mon_mode(interface)
@@ -156,19 +156,19 @@
             if ' - Address:' in line: # first line in iwlist scan for a new AP
                count += 1
         scanned_aps.append((count, iface))
-        print '['+G+'+'+W+'] Networks discovered by '+G+iface+W+': '+T+str(count)+W
+        print('['+G+'+'+W+'] Networks discovered by '+G+iface+W+': '+T+str(count)+W)
     try:
         interface = max(scanned_aps)[1]
         return interface
     except Exception as e:
         for iface in interfaces:
             interface = iface
-            print '['+R+'-'+W+'] Minor error:',e
-            print '    Starting monitor mode on '+G+interface+W
+            print('['+R+'-'+W+'] Minor error:',e)
+            print('    Starting monitor mode on '+G+interface+W)
             return interface
 
 def start_mon_mode(interface):
-    print '['+G+'+'+W+'] Starting monitor mode off '+G+interface+W
+    print('['+G+'+'+W+'] Starting monitor mode off '+G+interface+W)
     try:
         os.system('ip link set %s down' % interface)
         os.system('iwconfig %s mode monitor' % interface)
@@ -189,7 +189,7 @@
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', mon_iface[:15]))
     mac = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
-    print '['+G+'*'+W+'] Monitor mode: '+G+mon_iface+W+' - '+O+mac+W
+    print('['+G+'*'+W+'] Monitor mode: '+G+mon_iface+W+' - '+O+mac+W)
     return mac
 
 ########################################
@@ -224,7 +224,7 @@
             try:
                 proc = Popen(['iw', 'dev', mon_iface, 'set', 'channel', monchannel], stdout=DN, stderr=PIPE)
             except OSError:
-                print '['+R+'-'+W+'] Could not execute "iw"'
+                print('['+R+'-'+W+'] Could not execute "iw"')
                 os.kill(os.getpid(),SIGINT)
                 sys.exit(1)
             for line in proc.communicate()[1].split('\n'):
@@ -289,26 +289,26 @@
 def output(err, monchannel):
     os.system('clear')
     if args.dry_run:
-        print P+'***DRY-RUN***'+W
+        print(P+'***DRY-RUN***'+W)
     if err:
-        print err
+        print(err)
     else:
-        print '['+G+'+'+W+'] '+mon_iface+' channel: '+G+monchannel+W+'\n'
+        print('['+G+'+'+W+'] '+mon_iface+' channel: '+G+monchannel+W+'\n')
     if len(clients_APs) > 0:
-        print '                  Deauthing                 ch   ESSID'
+        print('                  Deauthing                 ch   ESSID')
     # Print the deauth list
     with lock:
         for ca in clients_APs:
             if len(ca) > 3:
-                print '['+T+'*'+W+'] '+O+ca[0]+W+' - '+O+ca[1]+W+' - '+ca[2].ljust(2)+' - '+T+ca[3]+W
+                print('['+T+'*'+W+'] '+O+ca[0]+W+' - '+O+ca[1]+W+' - '+ca[2].ljust(2)+' - '+T+ca[3]+W)
             else:
-                print '['+T+'*'+W+'] '+O+ca[0]+W+' - '+O+ca[1]+W+' - '+ca[2]
+                print('['+T+'*'+W+'] '+O+ca[0]+W+' - '+O+ca[1]+W+' - '+ca[2])
     if len(APs) > 0:
-        print '\n      Access Points     ch   ESSID'
+        print('\n      Access Points     ch   ESSID')
     with lock:
         for ap in APs:
-            print '['+T+'*'+W+'] '+O+ap[0]+W+' - '+ap[1].ljust(2)+' - '+T+ap[2]+W
-    print ''
+            print('['+T+'*'+W+'] '+O+ap[0]+W+' - '+ap[1].ljust(2)+' - '+T+ap[2]+W)
+    print('')
 
 def noise_filter(skip, addr1, addr2):
     # Broadcast, broadcast, IPv6mcast, spanning tree, spanning tree, multicast, broadcast
@@ -464,5 +464,5 @@
     except Exception as msg:
         remove_mon_iface(mon_iface)
         os.system('service network-manager restart')
-        print '\n['+R+'!'+W+'] Closing'
+        print('\n['+R+'!'+W+'] Closing')
         sys.exit(0)
