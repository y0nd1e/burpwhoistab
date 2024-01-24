from burp import IBurpExtender, ITab, IContextMenuFactory
from javax.swing import JPanel, JLabel, JTextField, JButton, JTextArea, JScrollPane, GroupLayout, JMenuItem
from java.awt import Dimension, EventQueue
from java.awt.event import ActionListener
from java.net import URL
import json
import urllib2

class BurpExtender(IBurpExtender, ITab, IContextMenuFactory):
    # Hardcode the API key here
    API_KEY = "APIKEY"

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("WHOIS Lookup")
        
        # Create Swing components
        self._panel = JPanel()
        self._domainLabel = JLabel("Domain:")
        self._domainField = JTextField(20)
        self._lookupButton = JButton("Lookup", actionPerformed=self.lookupAction)
        self._responseArea = JTextArea()
        self._responseArea.setEditable(False)
        self._responseScroll = JScrollPane(self._responseArea)
        self._responseScroll.setPreferredSize(Dimension(600, 400))

        # Layout setup
        self.setupLayout()

        # Register the custom tab and context menu
        callbacks.addSuiteTab(self)
        callbacks.registerContextMenuFactory(self)

    def setupLayout(self):
        layout = GroupLayout(self._panel)
        self._panel.setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)

        layout.setHorizontalGroup(
            layout.createParallelGroup()
            .addGroup(layout.createSequentialGroup()
                .addComponent(self._domainLabel)
                .addComponent(self._domainField)
                .addComponent(self._lookupButton))
            .addComponent(self._responseScroll)
        )

        layout.setVerticalGroup(
            layout.createSequentialGroup()
            .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                .addComponent(self._domainLabel)
                .addComponent(self._domainField)
                .addComponent(self._lookupButton))
            .addComponent(self._responseScroll)
        )

    def getTabCaption(self):
        return "WHOIS Lookup"

    def getUiComponent(self):
        return self._panel

    def createMenuItems(self, contextMenuInvocation):
        self.contextMenuInvocation = contextMenuInvocation
        menuList = []
        menuItem = JMenuItem("Send to WHOIS Lookup", actionPerformed=self.menuItemClicked)
        menuList.append(menuItem)
        return menuList

    def menuItemClicked(self, event):
        httpRequestResponse = self.contextMenuInvocation.getSelectedMessages()[0]
        url = httpRequestResponse.getHttpService().getHost()
        
        # Update the domain field in the Event Dispatch Thread
        def run():
            self._domainField.setText(url)
        
        EventQueue.invokeLater(run)

    def lookupAction(self, event):
        # Use the hardcoded API key
        apiKey = BurpExtender.API_KEY
        domain = self._domainField.getText()
        whoisInfo = self.getWhoisInfo(apiKey, domain)
        self._responseArea.setText(whoisInfo)

    def getWhoisInfo(self, apiKey, domain):
        whoisUrl = "https://api.whoisfreaks.com/v1.0/whois?apiKey={}&whois=live&domainName={}".format(apiKey, domain)
        try:
            response = urllib2.urlopen(whoisUrl).read()
            jsonResponse = json.loads(response)
            return json.dumps(jsonResponse, indent=4)
        except Exception as e:
            return "Error fetching WHOIS data for {}: {}".format(domain, str(e))
