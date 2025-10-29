# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1l111l1l1_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11111ll1ll_opy_, bstack1lll11111l_opy_, update, bstack1111l111l1_opy_,
                                       bstack1111l1lll1_opy_, bstack1lll1lllll_opy_, bstack11lllllll1_opy_, bstack1l1l1l11l_opy_,
                                       bstack11ll1l11l_opy_, bstack1111lllll1_opy_, bstack1l1ll1l11l_opy_,
                                       bstack11l11lllll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack111l1ll1ll_opy_)
from browserstack_sdk.bstack11111ll1_opy_ import bstack1llll1lll_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11l1l11ll1_opy_
from bstack_utils.capture import bstack1l111lll_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack111ll1l11l_opy_, bstack1l1ll11111_opy_, bstack1ll11111ll_opy_, \
    bstack111ll11lll_opy_
from bstack_utils.helper import bstack1l11l111_opy_, bstack111l1l11111_opy_, bstack1l1lllll_opy_, bstack11lll11l1_opy_, bstack1lll1l11l11_opy_, bstack1ll1ll1l_opy_, \
    bstack1111lll1l1l_opy_, \
    bstack1111ll1111l_opy_, bstack11l11l111_opy_, bstack1111l1111l_opy_, bstack1111l1lll11_opy_, bstack11ll1l1l1_opy_, Notset, \
    bstack1lllll1ll1_opy_, bstack1111l1111ll_opy_, bstack111l11l11l1_opy_, Result, bstack1111llll111_opy_, bstack111l111111l_opy_, error_handler, \
    bstack11l1111ll_opy_, bstack1l1ll1l1l_opy_, bstack11lll1l11_opy_, bstack111l1l1111l_opy_
from bstack_utils.bstack11l1ll1111l_opy_ import bstack11l1l1lllll_opy_
from bstack_utils.messages import bstack1l1lll11l_opy_, bstack111l1l1l1l_opy_, bstack1l11l11l1l_opy_, bstack111l111111_opy_, bstack111ll1ll_opy_, \
    bstack11l1l1ll11_opy_, bstack11lll111l_opy_, bstack1ll1ll111l_opy_, bstack1ll11111l_opy_, bstack1l1l11l111_opy_, \
    bstack1ll11lll11_opy_, bstack1l11111l11_opy_, bstack1l1ll111l1_opy_
from bstack_utils.proxy import bstack1l11ll111l_opy_, bstack111ll1ll1_opy_
from bstack_utils.bstack111ll11ll1_opy_ import bstack11l111l11ll_opy_, bstack11l111l1l11_opy_, bstack11l111l1ll1_opy_, bstack11l1111lll1_opy_, \
    bstack11l111l111l_opy_, bstack11l111ll11l_opy_, bstack11l111l11l1_opy_, bstack11l1l1l11l_opy_, bstack11l111l1l1l_opy_
from bstack_utils.bstack1ll111111l_opy_ import bstack11l1lll1l1_opy_
from bstack_utils.bstack1ll11lll1l_opy_ import bstack1l111111l1_opy_, bstack1l111l1lll_opy_, bstack1ll1l111l_opy_, \
    bstack111l1l11l1_opy_, bstack1ll111l1l1_opy_
from bstack_utils.bstack1ll1llll_opy_ import bstack1l11l1ll_opy_
from bstack_utils.bstack1l11ll11_opy_ import bstack1l1l111l_opy_
import bstack_utils.accessibility as bstack111l1ll1_opy_
from bstack_utils.bstack1l1l11ll_opy_ import bstack1ll1ll11_opy_
from bstack_utils.bstack111llll11_opy_ import bstack111llll11_opy_
from bstack_utils.bstack1llll1l1l_opy_ import bstack111ll11l_opy_
from browserstack_sdk.__init__ import bstack111l1l111_opy_
from browserstack_sdk.sdk_cli.bstack1l11lllll1l_opy_ import bstack1l1l1ll1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll_opy_ import bstack1lll1l1lll_opy_, Events, bstack1l1111ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l1llll111l_opy_, bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1lll1l1lll_opy_ import bstack1lll1l1lll_opy_, Events, bstack1l1111ll1_opy_
bstack1l11111ll_opy_ = None
bstack1l1llll1l_opy_ = None
bstack1ll1l1lll_opy_ = None
bstack11lll11ll1_opy_ = None
bstack1111111ll_opy_ = None
bstack11ll1ll1l1_opy_ = None
bstack1llll11l1l_opy_ = None
bstack11llllll1l_opy_ = None
bstack111lllll1_opy_ = None
bstack1ll1lllll1_opy_ = None
bstack1l11l11ll_opy_ = None
bstack111l111l1l_opy_ = None
bstack111l11111_opy_ = None
bstack1ll11l111l_opy_ = bstack11l11ll_opy_ (u"ࠩࠪ⊒")
CONFIG = {}
bstack1l1llll1ll_opy_ = False
bstack11l1l1111_opy_ = bstack11l11ll_opy_ (u"ࠪࠫ⊓")
bstack11lllll1ll_opy_ = bstack11l11ll_opy_ (u"ࠫࠬ⊔")
bstack1llll1lll1_opy_ = False
bstack1l1l1l111l_opy_ = []
bstack11lll1lll1_opy_ = bstack111ll1l11l_opy_
bstack1lll1llll11l_opy_ = bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⊕")
bstack11111ll1l1_opy_ = {}
bstack1l1l1l1ll1_opy_ = None
bstack1l11lll11_opy_ = False
logger = bstack11l1l11ll1_opy_.get_logger(__name__, bstack11lll1lll1_opy_)
store = {
    bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⊖"): []
}
bstack1lll1lll1ll1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1lll1l11_opy_ = {}
current_test_uuid = None
cli_context = bstack1l1llll111l_opy_(
    test_framework_name=bstack1ll1ll1l1l_opy_[bstack11l11ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࠭ࡃࡆࡇࠫ⊗")] if bstack11ll1l1l1_opy_() else bstack1ll1ll1l1l_opy_[bstack11l11ll_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࠨ⊘")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1l1l111lll_opy_(page, bstack11l11ll1l_opy_):
    try:
        page.evaluate(bstack11l11ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ⊙"),
                      bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧ⊚") + json.dumps(
                          bstack11l11ll1l_opy_) + bstack11l11ll_opy_ (u"ࠦࢂࢃࠢ⊛"))
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥ⊜"), e)
def bstack111ll1l1ll_opy_(page, message, level):
    try:
        page.evaluate(bstack11l11ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ⊝"), bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ⊞") + json.dumps(
            message) + bstack11l11ll_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫ⊟") + json.dumps(level) + bstack11l11ll_opy_ (u"ࠩࢀࢁࠬ⊠"))
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨ⊡"), e)
def pytest_configure(config):
    global bstack11l1l1111_opy_
    global CONFIG
    bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
    config.args = bstack1l1l111l_opy_.bstack11l111llll1_opy_(config.args)
    bstack1lll11111_opy_.bstack11l11ll11l_opy_(bstack11lll1l11_opy_(config.getoption(bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ⊢"))))
    try:
        bstack11l1l11ll1_opy_.bstack11111l11lll_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1lll1l1lll_opy_.invoke(Events.CONNECT, bstack1l1111ll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⊣"), bstack11l11ll_opy_ (u"࠭࠰ࠨ⊤")))
        config = json.loads(os.environ.get(bstack11l11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࠨ⊥"), bstack11l11ll_opy_ (u"ࠣࡽࢀࠦ⊦")))
        cli.bstack1l1l1llllll_opy_(bstack1111l1111l_opy_(bstack11l1l1111_opy_, CONFIG), cli_context.platform_index, bstack1111l111l1_opy_)
    if cli.bstack1l1l11l1l1l_opy_(bstack1l1l1ll1l1l_opy_):
        cli.bstack1l1l1111lll_opy_()
        logger.debug(bstack11l11ll_opy_ (u"ࠤࡆࡐࡎࠦࡩࡴࠢࡤࡧࡹ࡯ࡶࡦࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣ⊧") + str(cli_context.platform_index) + bstack11l11ll_opy_ (u"ࠥࠦ⊨"))
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.BEFORE_ALL, bstack1lll1l1llll_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11l11ll_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤ⊩"), None)
    if cli.is_running() and when == bstack11l11ll_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ⊪"):
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.LOG_REPORT, bstack1lll1l1llll_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11l11ll_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ⊫"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⊬")))
        if not passed:
            config = json.loads(os.environ.get(bstack11l11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢ⊭"), bstack11l11ll_opy_ (u"ࠤࡾࢁࠧ⊮")))
            if bstack111ll11l_opy_.bstack111ll111_opy_(config):
                bstack1lllll1llll1_opy_ = bstack111ll11l_opy_.bstack1lll1l1l1_opy_(config)
                if item.execution_count > bstack1lllll1llll1_opy_:
                    print(bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡳࡧࡷࡶ࡮࡫ࡳ࠻ࠢࠪ⊯"), report.nodeid, os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⊰")))
                    bstack111ll11l_opy_.bstack111lll1llll_opy_(report.nodeid)
            else:
                print(bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࠬ⊱"), report.nodeid, os.environ.get(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⊲")))
                bstack111ll11l_opy_.bstack111lll1llll_opy_(report.nodeid)
        else:
            print(bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࠥࡶࡡࡴࡵࡨࡨ࠿ࠦࠧ⊳"), report.nodeid, os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⊴")))
    if cli.is_running():
        if when == bstack11l11ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣ⊵"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.BEFORE_EACH, bstack1lll1l1llll_opy_.POST, item, call, outcome)
        elif when == bstack11l11ll_opy_ (u"ࠥࡧࡦࡲ࡬ࠣ⊶"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.LOG_REPORT, bstack1lll1l1llll_opy_.POST, item, call, outcome)
        elif when == bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ⊷"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.AFTER_EACH, bstack1lll1l1llll_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11l11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⊸"))
    plugins = item.config.getoption(bstack11l11ll_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢ⊹"))
    report = outcome.get_result()
    os.environ[bstack11l11ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ⊺")] = report.nodeid
    bstack1lll1ll111l1_opy_(item, call, report)
    if bstack11l11ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳࠨ⊻") not in plugins or bstack11ll1l1l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack11l11ll_opy_ (u"ࠤࡢࡨࡷ࡯ࡶࡦࡴࠥ⊼"), None)
    page = getattr(item, bstack11l11ll_opy_ (u"ࠥࡣࡵࡧࡧࡦࠤ⊽"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1lll1lll_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName)
def bstack1lll1lll1lll_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⊾") and report.skipped:
        bstack11l111l1l1l_opy_(report)
    if report.when in [bstack11l11ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ⊿"), bstack11l11ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ⋀")]:
        return
    if not bstack1lll1l11l11_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11l11ll_opy_ (u"ࠧࡵࡴࡸࡩࠬ⋁")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭⋂") + json.dumps(
                    report.nodeid) + bstack11l11ll_opy_ (u"ࠩࢀࢁࠬ⋃"))
        os.environ[bstack11l11ll_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⋄")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11l11ll_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࡀࠠࡼ࠲ࢀࠦ⋅").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢ⋆")))
    bstack1l1l111l11_opy_ = bstack11l11ll_opy_ (u"ࠨࠢ⋇")
    bstack11l111l1l1l_opy_(report)
    if not passed:
        try:
            bstack1l1l111l11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11l11ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢ⋈").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1l111l11_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⋉")))
        bstack1l1l111l11_opy_ = bstack11l11ll_opy_ (u"ࠤࠥ⋊")
        if not passed:
            try:
                bstack1l1l111l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l11ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ⋋").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1l111l11_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨ⋌")
                    + json.dumps(bstack11l11ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠦࠨ⋍"))
                    + bstack11l11ll_opy_ (u"ࠨ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤ⋎")
                )
            else:
                item._driver.execute_script(
                    bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬ⋏")
                    + json.dumps(str(bstack1l1l111l11_opy_))
                    + bstack11l11ll_opy_ (u"ࠣ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠦ⋐")
                )
        except Exception as e:
            summary.append(bstack11l11ll_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡢࡰࡱࡳࡹࡧࡴࡦ࠼ࠣࡿ࠵ࢃࠢ⋑").format(e))
def bstack1lll1ll1l1l1_opy_(test_name, error_message):
    try:
        bstack1lll1lll11l1_opy_ = []
        bstack11lll1ll11_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ⋒"), bstack11l11ll_opy_ (u"ࠫ࠵࠭⋓"))
        bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⋔"): test_name, bstack11l11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⋕"): error_message, bstack11l11ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭⋖"): bstack11lll1ll11_opy_}
        bstack1lll1lll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭⋗"))
        if os.path.exists(bstack1lll1lll1l11_opy_):
            with open(bstack1lll1lll1l11_opy_) as f:
                bstack1lll1lll11l1_opy_ = json.load(f)
        bstack1lll1lll11l1_opy_.append(bstack11lll1l1l1_opy_)
        with open(bstack1lll1lll1l11_opy_, bstack11l11ll_opy_ (u"ࠩࡺࠫ⋘")) as f:
            json.dump(bstack1lll1lll11l1_opy_, f)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡥࡳࡵ࡬ࡷࡹ࡯࡮ࡨࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡰࡺࡶࡨࡷࡹࠦࡥࡳࡴࡲࡶࡸࡀࠠࠨ⋙") + str(e))
def bstack1lll1lll11ll_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11l11ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ⋚"), bstack11l11ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ⋛")]:
        return
    if (str(skipSessionName).lower() != bstack11l11ll_opy_ (u"࠭ࡴࡳࡷࡨࠫ⋜")):
        bstack1l1l111lll_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l11ll_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ⋝")))
    bstack1l1l111l11_opy_ = bstack11l11ll_opy_ (u"ࠣࠤ⋞")
    bstack11l111l1l1l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1l111l11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l11ll_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ⋟").format(e)
                )
        try:
            if passed:
                bstack1ll111l1l1_opy_(getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⋠"), None), bstack11l11ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ⋡"))
            else:
                error_message = bstack11l11ll_opy_ (u"ࠬ࠭⋢")
                if bstack1l1l111l11_opy_:
                    bstack111ll1l1ll_opy_(item._page, str(bstack1l1l111l11_opy_), bstack11l11ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ⋣"))
                    bstack1ll111l1l1_opy_(getattr(item, bstack11l11ll_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭⋤"), None), bstack11l11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ⋥"), str(bstack1l1l111l11_opy_))
                    error_message = str(bstack1l1l111l11_opy_)
                else:
                    bstack1ll111l1l1_opy_(getattr(item, bstack11l11ll_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⋦"), None), bstack11l11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ⋧"))
                bstack1lll1ll1l1l1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11l11ll_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀ࠶ࡽࠣ⋨").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11l11ll_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ⋩"), default=bstack11l11ll_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧ⋪"), help=bstack11l11ll_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨ⋫"))
    parser.addoption(bstack11l11ll_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ⋬"), default=bstack11l11ll_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣ⋭"), help=bstack11l11ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤ⋮"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11l11ll_opy_ (u"ࠦ࠲࠳ࡤࡳ࡫ࡹࡩࡷࠨ⋯"), action=bstack11l11ll_opy_ (u"ࠧࡹࡴࡰࡴࡨࠦ⋰"), default=bstack11l11ll_opy_ (u"ࠨࡣࡩࡴࡲࡱࡪࠨ⋱"),
                         help=bstack11l11ll_opy_ (u"ࠢࡅࡴ࡬ࡺࡪࡸࠠࡵࡱࠣࡶࡺࡴࠠࡵࡧࡶࡸࡸࠨ⋲"))
def bstack1ll1lll1_opy_(log):
    if not (log[bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⋳")] and log[bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⋴")].strip()):
        return
    active = bstack1lll1lll_opy_()
    log = {
        bstack11l11ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⋵"): log[bstack11l11ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⋶")],
        bstack11l11ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⋷"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"࡚࠭ࠨ⋸"),
        bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⋹"): log[bstack11l11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⋺")],
    }
    if active:
        if active[bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⋻")] == bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⋼"):
            log[bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋽")] = active[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⋾")]
        elif active[bstack11l11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋿")] == bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࠬ⌀"):
            log[bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⌁")] = active[bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⌂")]
    bstack1ll1ll11_opy_.bstack1ll1l111_opy_([log])
def bstack1lll1lll_opy_():
    if len(store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⌃")]) > 0 and store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⌄")][-1]:
        return {
            bstack11l11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⌅"): bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⌆"),
            bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⌇"): store[bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⌈")][-1]
        }
    if store.get(bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⌉"), None):
        return {
            bstack11l11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ⌊"): bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ⌋"),
            bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⌌"): store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⌍")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.INIT_TEST, bstack1lll1l1llll_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.INIT_TEST, bstack1lll1l1llll_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1ll11l11_opy_ = True
        bstack11lll1lll_opy_ = bstack111l1ll1_opy_.bstack111l1lll1_opy_(bstack1111ll1111l_opy_(item.own_markers))
        if not cli.bstack1l1l11l1l1l_opy_(bstack1l1l1ll1l1l_opy_):
            item._a11y_test_case = bstack11lll1lll_opy_
            if bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⌎"), None):
                driver = getattr(item, bstack11l11ll_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⌏"), None)
                item._a11y_started = bstack111l1ll1_opy_.bstack1ll1l1l111_opy_(driver, bstack11lll1lll_opy_)
        if not bstack1ll1ll11_opy_.on() or bstack1lll1llll11l_opy_ != bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ⌐"):
            return
        global current_test_uuid #, bstack1l111111_opy_
        bstack11lll1l1_opy_ = {
            bstack11l11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⌑"): uuid4().__str__(),
            bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⌒"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠬࡠࠧ⌓")
        }
        current_test_uuid = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⌔")]
        store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⌕")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⌖")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1lll1l11_opy_[item.nodeid] = {**_1lll1l11_opy_[item.nodeid], **bstack11lll1l1_opy_}
        bstack1lll1lll111l_opy_(item, _1lll1l11_opy_[item.nodeid], bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⌗"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡧࡦࡲ࡬࠻ࠢࡾࢁࠬ⌘"), str(err))
def pytest_runtest_setup(item):
    store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⌙")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.BEFORE_EACH, bstack1lll1l1llll_opy_.PRE, item, bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⌚"))
    if bstack111ll11l_opy_.bstack111lll1lll1_opy_():
            bstack1lll1ll11l1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡡࡴࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥ⌛")
            logger.error(bstack1lll1ll11l1l_opy_)
            bstack11lll1l1_opy_ = {
                bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⌜"): uuid4().__str__(),
                bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⌝"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫ⌞"),
                bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⌟"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠫ࡟࠭⌠"),
                bstack11l11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⌡"): bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⌢"),
                bstack11l11ll_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ⌣"): bstack1lll1ll11l1l_opy_,
                bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⌤"): [],
                bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ⌥"): []
            }
            bstack1lll1lll111l_opy_(item, bstack11lll1l1_opy_, bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫ⌦"))
            pytest.skip(bstack1lll1ll11l1l_opy_)
            return # skip all existing operations
    global bstack1lll1lll1ll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1111l1lll11_opy_():
        atexit.register(bstack1llllll1l1_opy_)
        if not bstack1lll1lll1ll1_opy_:
            try:
                bstack1lll1ll1ll1l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111l1l1111l_opy_():
                    bstack1lll1ll1ll1l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1ll1ll1l_opy_:
                    signal.signal(s, bstack1lll1llll1ll_opy_)
                bstack1lll1lll1ll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11l11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡩ࡬ࡷࡹ࡫ࡲࠡࡵ࡬࡫ࡳࡧ࡬ࠡࡪࡤࡲࡩࡲࡥࡳࡵ࠽ࠤࠧ⌧") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111l11ll_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11l11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⌨")
    try:
        if not bstack1ll1ll11_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack11lll1l1_opy_ = {
            bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ〈"): uuid,
            bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ〉"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠨ࡜ࠪ⌫"),
            bstack11l11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⌬"): bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⌭"),
            bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ⌮"): bstack11l11ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪ⌯"),
            bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⌰"): bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⌱")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11l11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⌲")] = item
        store[bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⌳")] = [uuid]
        if not _1lll1l11_opy_.get(item.nodeid, None):
            _1lll1l11_opy_[item.nodeid] = {bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⌴"): [], bstack11l11ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⌵"): []}
        _1lll1l11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⌶")].append(bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⌷")])
        _1lll1l11_opy_[item.nodeid + bstack11l11ll_opy_ (u"ࠧ࠮ࡵࡨࡸࡺࡶࠧ⌸")] = bstack11lll1l1_opy_
        bstack1lll1ll1l1ll_opy_(item, bstack11lll1l1_opy_, bstack11l11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⌹"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬ⌺"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.AFTER_EACH, bstack1lll1l1llll_opy_.PRE, item, bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ⌻"))
        return # skip all existing operations
    try:
        global bstack11111ll1l1_opy_
        bstack11lll1ll11_opy_ = 0
        if bstack1llll1lll1_opy_ is True:
            bstack11lll1ll11_opy_ = int(os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⌼")))
        if bstack11lll11111_opy_.bstack1111ll1l11_opy_() == bstack11l11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥ⌽"):
            if bstack11lll11111_opy_.bstack1ll11llll_opy_() == bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣ⌾"):
                bstack1lll1ll1l11l_opy_ = bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⌿"), None)
                bstack11ll11l1l1_opy_ = bstack1lll1ll1l11l_opy_ + bstack11l11ll_opy_ (u"ࠣ࠯ࡷࡩࡸࡺࡣࡢࡵࡨࠦ⍀")
                driver = getattr(item, bstack11l11ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⍁"), None)
                bstack1ll11llll1_opy_ = getattr(item, bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ⍂"), None)
                bstack1l1lll111l_opy_ = getattr(item, bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍃"), None)
                PercySDK.screenshot(driver, bstack11ll11l1l1_opy_, bstack1ll11llll1_opy_=bstack1ll11llll1_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack11111l11ll_opy_=bstack11lll1ll11_opy_)
        if not cli.bstack1l1l11l1l1l_opy_(bstack1l1l1ll1l1l_opy_):
            if getattr(item, bstack11l11ll_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺࡡࡳࡶࡨࡨࠬ⍄"), False):
                bstack1llll1lll_opy_.bstack111l11l1_opy_(getattr(item, bstack11l11ll_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧ⍅"), None), bstack11111ll1l1_opy_, logger, item)
        if not bstack1ll1ll11_opy_.on():
            return
        bstack11lll1l1_opy_ = {
            bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍆"): uuid4().__str__(),
            bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍇"): bstack1l1lllll_opy_().isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫ⍈"),
            bstack11l11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ⍉"): bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⍊"),
            bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⍋"): bstack11l11ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ⍌"),
            bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ⍍"): bstack11l11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ⍎")
        }
        _1lll1l11_opy_[item.nodeid + bstack11l11ll_opy_ (u"ࠩ࠰ࡸࡪࡧࡲࡥࡱࡺࡲࠬ⍏")] = bstack11lll1l1_opy_
        bstack1lll1ll1l1ll_opy_(item, bstack11lll1l1_opy_, bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⍐"))
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡀࠠࡼࡿࠪ⍑"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l1111lll1_opy_(fixturedef.argname):
        store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫ⍒")] = request.node
    elif bstack11l111l111l_opy_(fixturedef.argname):
        store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫ⍓")] = request.node
    if not bstack1ll1ll11_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.SETUP_FIXTURE, bstack1lll1l1llll_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.SETUP_FIXTURE, bstack1lll1l1llll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.SETUP_FIXTURE, bstack1lll1l1llll_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.SETUP_FIXTURE, bstack1lll1l1llll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⍔"): fixturedef.argname,
            bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⍕"): bstack1111lll1l1l_opy_(outcome),
            bstack11l11ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ⍖"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⍗")]
        if not _1lll1l11_opy_.get(current_test_item.nodeid, None):
            _1lll1l11_opy_[current_test_item.nodeid] = {bstack11l11ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⍘"): []}
        _1lll1l11_opy_[current_test_item.nodeid][bstack11l11ll_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⍙")].append(fixture)
    except Exception as err:
        logger.debug(bstack11l11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩ⍚"), str(err))
if bstack11ll1l1l1_opy_() and bstack1ll1ll11_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.STEP, bstack1lll1l1llll_opy_.PRE, request, step)
            return
        try:
            _1lll1l11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⍛")].bstack11l1l1l1_opy_(id(step))
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭⍜"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.STEP, bstack1lll1l1llll_opy_.POST, request, step, exception)
            return
        try:
            _1lll1l11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⍝")].bstack1l11llll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧ⍞"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.STEP, bstack1lll1l1llll_opy_.POST, request, step)
            return
        try:
            bstack1ll1llll_opy_: bstack1l11l1ll_opy_ = _1lll1l11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍟")]
            bstack1ll1llll_opy_.bstack1l11llll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩ⍠"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1llll11l_opy_
        try:
            if not bstack1ll1ll11_opy_.on() or bstack1lll1llll11l_opy_ != bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ⍡"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.TEST, bstack1lll1l1llll_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭⍢"), None)
            if not _1lll1l11_opy_.get(request.node.nodeid, None):
                _1lll1l11_opy_[request.node.nodeid] = {}
            bstack1ll1llll_opy_ = bstack1l11l1ll_opy_.bstack111111l111l_opy_(
                scenario, feature, request.node,
                name=bstack11l111ll11l_opy_(request.node, scenario),
                started_at=bstack1ll1ll1l_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11l11ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪ⍣"),
                tags=bstack11l111l11l1_opy_(feature, scenario),
                bstack1llll1ll_opy_=bstack1ll1ll11_opy_.bstack1l1l1lll_opy_(driver) if driver and driver.session_id else {}
            )
            _1lll1l11_opy_[request.node.nodeid][bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⍤")] = bstack1ll1llll_opy_
            bstack1lll1llllll1_opy_(bstack1ll1llll_opy_.uuid)
            bstack1ll1ll11_opy_.bstack11lllll1_opy_(bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⍥"), bstack1ll1llll_opy_)
        except Exception as err:
            print(bstack11l11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭⍦"), str(err))
def bstack1lll1lllll11_opy_(bstack11l1l111_opy_):
    if bstack11l1l111_opy_ in store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⍧")]:
        store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⍨")].remove(bstack11l1l111_opy_)
def bstack1lll1llllll1_opy_(test_uuid):
    store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⍩")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1ll1ll11_opy_.bstack1llll11l11ll_opy_
def bstack1lll1ll111l1_opy_(item, call, report):
    logger.debug(bstack11l11ll_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡳࡶࠪ⍪"))
    global bstack1lll1llll11l_opy_
    bstack1l111l11l1_opy_ = bstack1ll1ll1l_opy_()
    if hasattr(report, bstack11l11ll_opy_ (u"ࠩࡶࡸࡴࡶࠧ⍫")):
        bstack1l111l11l1_opy_ = bstack1111llll111_opy_(report.stop)
    elif hasattr(report, bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࠩ⍬")):
        bstack1l111l11l1_opy_ = bstack1111llll111_opy_(report.start)
    try:
        if getattr(report, bstack11l11ll_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍭"), bstack11l11ll_opy_ (u"ࠬ࠭⍮")) == bstack11l11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ⍯"):
            logger.debug(bstack11l11ll_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡴࡦࠢ࠰ࠤࢀࢃࠬࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࠲ࠦࡻࡾࠩ⍰").format(getattr(report, bstack11l11ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⍱"), bstack11l11ll_opy_ (u"ࠩࠪ⍲")).__str__(), bstack1lll1llll11l_opy_))
            if bstack1lll1llll11l_opy_ == bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⍳"):
                _1lll1l11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⍴")] = bstack1l111l11l1_opy_
                bstack1lll1lll111l_opy_(item, _1lll1l11_opy_[item.nodeid], bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⍵"), report, call)
                store[bstack11l11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⍶")] = None
            elif bstack1lll1llll11l_opy_ == bstack11l11ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦ⍷"):
                bstack1ll1llll_opy_ = _1lll1l11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⍸")]
                bstack1ll1llll_opy_.set(hooks=_1lll1l11_opy_[item.nodeid].get(bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⍹"), []))
                exception, bstack1llll1l1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1llll1l1_opy_ = [call.excinfo.exconly(), getattr(report, bstack11l11ll_opy_ (u"ࠪࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠩ⍺"), bstack11l11ll_opy_ (u"ࠫࠬ⍻"))]
                bstack1ll1llll_opy_.stop(time=bstack1l111l11l1_opy_, result=Result(result=getattr(report, bstack11l11ll_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭⍼"), bstack11l11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⍽")), exception=exception, bstack1llll1l1_opy_=bstack1llll1l1_opy_))
                bstack1ll1ll11_opy_.bstack11lllll1_opy_(bstack11l11ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⍾"), _1lll1l11_opy_[item.nodeid][bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⍿")])
        elif getattr(report, bstack11l11ll_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⎀"), bstack11l11ll_opy_ (u"ࠪࠫ⎁")) in [bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⎂"), bstack11l11ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ⎃")]:
            logger.debug(bstack11l11ll_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡺࡥࠡ࠯ࠣࡿࢂ࠲ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࠱ࠥࢁࡽࠨ⎄").format(getattr(report, bstack11l11ll_opy_ (u"ࠧࡸࡪࡨࡲࠬ⎅"), bstack11l11ll_opy_ (u"ࠨࠩ⎆")).__str__(), bstack1lll1llll11l_opy_))
            bstack1ll1l1ll_opy_ = item.nodeid + bstack11l11ll_opy_ (u"ࠩ࠰ࠫ⎇") + getattr(report, bstack11l11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⎈"), bstack11l11ll_opy_ (u"ࠫࠬ⎉"))
            if getattr(report, bstack11l11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⎊"), False):
                hook_type = bstack11l11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ⎋") if getattr(report, bstack11l11ll_opy_ (u"ࠧࡸࡪࡨࡲࠬ⎌"), bstack11l11ll_opy_ (u"ࠨࠩ⎍")) == bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ⎎") else bstack11l11ll_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧ⎏")
                _1lll1l11_opy_[bstack1ll1l1ll_opy_] = {
                    bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⎐"): uuid4().__str__(),
                    bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⎑"): bstack1l111l11l1_opy_,
                    bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⎒"): hook_type
                }
            _1lll1l11_opy_[bstack1ll1l1ll_opy_][bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎓")] = bstack1l111l11l1_opy_
            bstack1lll1lllll11_opy_(_1lll1l11_opy_[bstack1ll1l1ll_opy_][bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⎔")])
            bstack1lll1ll1l1ll_opy_(item, _1lll1l11_opy_[bstack1ll1l1ll_opy_], bstack11l11ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⎕"), report, call)
            if getattr(report, bstack11l11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⎖"), bstack11l11ll_opy_ (u"ࠫࠬ⎗")) == bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⎘"):
                if getattr(report, bstack11l11ll_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ⎙"), bstack11l11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⎚")) == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⎛"):
                    bstack11lll1l1_opy_ = {
                        bstack11l11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⎜"): uuid4().__str__(),
                        bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⎝"): bstack1ll1ll1l_opy_(),
                        bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎞"): bstack1ll1ll1l_opy_()
                    }
                    _1lll1l11_opy_[item.nodeid] = {**_1lll1l11_opy_[item.nodeid], **bstack11lll1l1_opy_}
                    bstack1lll1lll111l_opy_(item, _1lll1l11_opy_[item.nodeid], bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⎟"))
                    bstack1lll1lll111l_opy_(item, _1lll1l11_opy_[item.nodeid], bstack11l11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⎠"), report, call)
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡾࢁࠬ⎡"), str(err))
def bstack1lll1ll1lll1_opy_(test, bstack11lll1l1_opy_, result=None, call=None, bstack1l11l1111l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1ll1llll_opy_ = {
        bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⎢"): bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⎣")],
        bstack11l11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ⎤"): bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ⎥"),
        bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⎦"): test.name,
        bstack11l11ll_opy_ (u"࠭ࡢࡰࡦࡼࠫ⎧"): {
            bstack11l11ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬ⎨"): bstack11l11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⎩"),
            bstack11l11ll_opy_ (u"ࠩࡦࡳࡩ࡫ࠧ⎪"): inspect.getsource(test.obj)
        },
        bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ⎫"): test.name,
        bstack11l11ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪ⎬"): test.name,
        bstack11l11ll_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬ⎭"): bstack1l1l111l_opy_.bstack1l111l1l_opy_(test),
        bstack11l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ⎮"): file_path,
        bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩ⎯"): file_path,
        bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⎰"): bstack11l11ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ⎱"),
        bstack11l11ll_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨ⎲"): file_path,
        bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⎳"): bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⎴")],
        bstack11l11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ⎵"): bstack11l11ll_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ⎶"),
        bstack11l11ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫ⎷"): {
            bstack11l11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭⎸"): test.nodeid
        },
        bstack11l11ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ⎹"): bstack1111ll1111l_opy_(test.own_markers)
    }
    if bstack1l11l1111l_opy_ in [bstack11l11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⎺"), bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⎻")]:
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"࠭࡭ࡦࡶࡤࠫ⎼")] = {
            bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⎽"): bstack11lll1l1_opy_.get(bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⎾"), [])
        }
    if bstack1l11l1111l_opy_ == bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ⎿"):
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏀")] = bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ⏁")
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⏂")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⏃")]
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⏄")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⏅")]
    if result:
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⏆")] = result.outcome
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⏇")] = result.duration * 1000
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏈")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏉")]
        if result.failed:
            bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ⏊")] = bstack1ll1ll11_opy_.bstack11111111ll_opy_(call.excinfo.typename)
            bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⏋")] = bstack1ll1ll11_opy_.bstack1llll11l1l11_opy_(call.excinfo, result)
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⏌")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⏍")]
    if outcome:
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏎")] = bstack1111lll1l1l_opy_(outcome)
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏏")] = 0
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏐")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏑")]
        if bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏒")] == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⏓"):
            bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⏔")] = bstack11l11ll_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫ⏕")  # bstack1lll1ll1llll_opy_
            bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ⏖")] = [{bstack11l11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⏗"): [bstack11l11ll_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪ⏘")]}]
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⏙")] = bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⏚")]
    return bstack1ll1llll_opy_
def bstack1lll1ll11ll1_opy_(test, bstack1lll1ll1_opy_, bstack1l11l1111l_opy_, result, call, outcome, bstack1lll1ll1l111_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⏛")]
    hook_name = bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭⏜")]
    hook_data = {
        bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⏝"): bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ⏞")],
        bstack11l11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ⏟"): bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ⏠"),
        bstack11l11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭⏡"): bstack11l11ll_opy_ (u"ࠩࡾࢁࠬ⏢").format(bstack11l111l1l11_opy_(hook_name)),
        bstack11l11ll_opy_ (u"ࠪࡦࡴࡪࡹࠨ⏣"): {
            bstack11l11ll_opy_ (u"ࠫࡱࡧ࡮ࡨࠩ⏤"): bstack11l11ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ⏥"),
            bstack11l11ll_opy_ (u"࠭ࡣࡰࡦࡨࠫ⏦"): None
        },
        bstack11l11ll_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭⏧"): test.name,
        bstack11l11ll_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ⏨"): bstack1l1l111l_opy_.bstack1l111l1l_opy_(test, hook_name),
        bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ⏩"): file_path,
        bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ⏪"): file_path,
        bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏫"): bstack11l11ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⏬"),
        bstack11l11ll_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ⏭"): file_path,
        bstack11l11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⏮"): bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⏯")],
        bstack11l11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ⏰"): bstack11l11ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬ⏱") if bstack1lll1llll11l_opy_ == bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨ⏲") else bstack11l11ll_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬ⏳"),
        bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⏴"): hook_type
    }
    bstack1l11111l11l_opy_ = bstack1l1l1111_opy_(_1lll1l11_opy_.get(test.nodeid, None))
    if bstack1l11111l11l_opy_:
        hook_data[bstack11l11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬ⏵")] = bstack1l11111l11l_opy_
    if result:
        hook_data[bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⏶")] = result.outcome
        hook_data[bstack11l11ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ⏷")] = result.duration * 1000
        hook_data[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏸")] = bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏹")]
        if result.failed:
            hook_data[bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⏺")] = bstack1ll1ll11_opy_.bstack11111111ll_opy_(call.excinfo.typename)
            hook_data[bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ⏻")] = bstack1ll1ll11_opy_.bstack1llll11l1l11_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏼")] = bstack1111lll1l1l_opy_(outcome)
        hook_data[bstack11l11ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⏽")] = 100
        hook_data[bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏾")] = bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏿")]
        if hook_data[bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ␀")] == bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ␁"):
            hook_data[bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ␂")] = bstack11l11ll_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨ␃")  # bstack1lll1ll1llll_opy_
            hook_data[bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ␄")] = [{bstack11l11ll_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ␅"): [bstack11l11ll_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧ␆")]}]
    if bstack1lll1ll1l111_opy_:
        hook_data[bstack11l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ␇")] = bstack1lll1ll1l111_opy_.result
        hook_data[bstack11l11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭␈")] = bstack1111l1111ll_opy_(bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ␉")], bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ␊")])
        hook_data[bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭␋")] = bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ␌")]
        if hook_data[bstack11l11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ␍")] == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ␎"):
            hook_data[bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ␏")] = bstack1ll1ll11_opy_.bstack11111111ll_opy_(bstack1lll1ll1l111_opy_.exception_type)
            hook_data[bstack11l11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ␐")] = [{bstack11l11ll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪ␑"): bstack111l11l11l1_opy_(bstack1lll1ll1l111_opy_.exception)}]
    return hook_data
def bstack1lll1lll111l_opy_(test, bstack11lll1l1_opy_, bstack1l11l1111l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11l11ll_opy_ (u"ࠨࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡧࡹࡩࡳࡺ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡸࡪࡹࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠠ࠮ࠢࡾࢁࠬ␒").format(bstack1l11l1111l_opy_))
    bstack1ll1llll_opy_ = bstack1lll1ll1lll1_opy_(test, bstack11lll1l1_opy_, result, call, bstack1l11l1111l_opy_, outcome)
    driver = getattr(test, bstack11l11ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ␓"), None)
    if bstack1l11l1111l_opy_ == bstack11l11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ␔") and driver:
        bstack1ll1llll_opy_[bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪ␕")] = bstack1ll1ll11_opy_.bstack1l1l1lll_opy_(driver)
    if bstack1l11l1111l_opy_ == bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭␖"):
        bstack1l11l1111l_opy_ = bstack11l11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ␗")
    bstack1ll11111_opy_ = {
        bstack11l11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ␘"): bstack1l11l1111l_opy_,
        bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ␙"): bstack1ll1llll_opy_
    }
    bstack1ll1ll11_opy_.bstack1ll1l1l1_opy_(bstack1ll11111_opy_)
    if bstack1l11l1111l_opy_ == bstack11l11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ␚"):
        threading.current_thread().bstackTestMeta = {bstack11l11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ␛"): bstack11l11ll_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ␜")}
    elif bstack1l11l1111l_opy_ == bstack11l11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ␝"):
        threading.current_thread().bstackTestMeta = {bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭␞"): getattr(result, bstack11l11ll_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨ␟"), bstack11l11ll_opy_ (u"ࠨࠩ␠"))}
def bstack1lll1ll1l1ll_opy_(test, bstack11lll1l1_opy_, bstack1l11l1111l_opy_, result=None, call=None, outcome=None, bstack1lll1ll1l111_opy_=None):
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡶࡩࡳࡪ࡟ࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡨࡺࡪࡴࡴ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤ࡭ࡵ࡯࡬ࠢࡧࡥࡹࡧࠬࠡࡧࡹࡩࡳࡺࡔࡺࡲࡨࠤ࠲ࠦࡻࡾࠩ␡").format(bstack1l11l1111l_opy_))
    hook_data = bstack1lll1ll11ll1_opy_(test, bstack11lll1l1_opy_, bstack1l11l1111l_opy_, result, call, outcome, bstack1lll1ll1l111_opy_)
    bstack1ll11111_opy_ = {
        bstack11l11ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ␢"): bstack1l11l1111l_opy_,
        bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭␣"): hook_data
    }
    bstack1ll1ll11_opy_.bstack1ll1l1l1_opy_(bstack1ll11111_opy_)
def bstack1l1l1111_opy_(bstack11lll1l1_opy_):
    if not bstack11lll1l1_opy_:
        return None
    if bstack11lll1l1_opy_.get(bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ␤"), None):
        return getattr(bstack11lll1l1_opy_[bstack11l11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ␥")], bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ␦"), None)
    return bstack11lll1l1_opy_.get(bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭␧"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.LOG, bstack1lll1l1llll_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_.LOG, bstack1lll1l1llll_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1ll1ll11_opy_.on():
            return
        places = [bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ␨"), bstack11l11ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ␩"), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭␪")]
        logs = []
        for bstack1lll1ll1ll11_opy_ in places:
            records = caplog.get_records(bstack1lll1ll1ll11_opy_)
            bstack1lll1lll1111_opy_ = bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ␫") if bstack1lll1ll1ll11_opy_ == bstack11l11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ␬") else bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ␭")
            bstack1lll1llll1l1_opy_ = request.node.nodeid + (bstack11l11ll_opy_ (u"ࠨࠩ␮") if bstack1lll1ll1ll11_opy_ == bstack11l11ll_opy_ (u"ࠩࡦࡥࡱࡲࠧ␯") else bstack11l11ll_opy_ (u"ࠪ࠱ࠬ␰") + bstack1lll1ll1ll11_opy_)
            test_uuid = bstack1l1l1111_opy_(_1lll1l11_opy_.get(bstack1lll1llll1l1_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111l111111l_opy_(record.message):
                    continue
                logs.append({
                    bstack11l11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ␱"): bstack111l1l11111_opy_(record.created).isoformat() + bstack11l11ll_opy_ (u"ࠬࡠࠧ␲"),
                    bstack11l11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ␳"): record.levelname,
                    bstack11l11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ␴"): record.message,
                    bstack1lll1lll1111_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1ll1ll11_opy_.bstack1ll1l111_opy_(logs)
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡦࡳࡳࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥ࠻ࠢࡾࢁࠬ␵"), str(err))
def bstack1ll1lll1ll_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l11lll11_opy_
    bstack1lll1l11ll_opy_ = bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭␶"), None) and bstack1l11l111_opy_(
            threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ␷"), None)
    bstack1ll1lll111_opy_ = getattr(driver, bstack11l11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ␸"), None) != None and getattr(driver, bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ␹"), None) == True
    if sequence == bstack11l11ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭␺") and driver != None:
      if not bstack1l11lll11_opy_ and bstack1lll1l11l11_opy_() and bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ␻") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ␼")] == True and bstack111llll11_opy_.bstack11l1ll1111_opy_(driver_command) and (bstack1ll1lll111_opy_ or bstack1lll1l11ll_opy_) and not bstack111l1ll1ll_opy_(args):
        try:
          bstack1l11lll11_opy_ = True
          logger.debug(bstack11l11ll_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡽࢀࠫ␽").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11l11ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡦࡴࡩࡳࡷࡳࠠࡴࡥࡤࡲࠥࢁࡽࠨ␾").format(str(err)))
        bstack1l11lll11_opy_ = False
    if sequence == bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪ␿"):
        if driver_command == bstack11l11ll_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ⑀"):
            bstack1ll1ll11_opy_.bstack1l1l1lll1l_opy_({
                bstack11l11ll_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ⑁"): response[bstack11l11ll_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭⑂")],
                bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⑃"): store[bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⑄")]
            })
def bstack1llllll1l1_opy_():
    global bstack1l1l1l111l_opy_
    bstack11l1l11ll1_opy_.bstack11l1l1l11_opy_()
    logging.shutdown()
    bstack1ll1ll11_opy_.bstack1lllll11_opy_()
    for driver in bstack1l1l1l111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1llll1ll_opy_(*args):
    global bstack1l1l1l111l_opy_
    bstack1ll1ll11_opy_.bstack1lllll11_opy_()
    for driver in bstack1l1l1l111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll1ll11ll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_, bstack1lll1ll1ll_opy_=bstack1l1l1l1ll1_opy_)
def bstack1l11111l1_opy_(self, *args, **kwargs):
    bstack1llll11lll_opy_ = bstack1l11111ll_opy_(self, *args, **kwargs)
    bstack1l11l1llll_opy_ = getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ⑅"), None)
    if bstack1l11l1llll_opy_ and bstack1l11l1llll_opy_.get(bstack11l11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⑆"), bstack11l11ll_opy_ (u"ࠬ࠭⑇")) == bstack11l11ll_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⑈"):
        bstack1ll1ll11_opy_.bstack1l111lll1l_opy_(self)
    return bstack1llll11lll_opy_
@measure(event_name=EVENTS.bstack1ll111111_opy_, stage=STAGE.bstack1l1111l111_opy_, bstack1lll1ll1ll_opy_=bstack1l1l1l1ll1_opy_)
def bstack1ll1l11l1l_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
    if bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ⑉")):
        return
    bstack1lll11111_opy_.set_property(bstack11l11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ⑊"), True)
    global bstack1ll11l111l_opy_
    global bstack1l1111ll11_opy_
    bstack1ll11l111l_opy_ = framework_name
    logger.info(bstack1l11111l11_opy_.format(bstack1ll11l111l_opy_.split(bstack11l11ll_opy_ (u"ࠩ࠰ࠫ⑋"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1l11l11_opy_():
            Service.start = bstack11lllllll1_opy_
            Service.stop = bstack1l1l1l11l_opy_
            webdriver.Remote.get = bstack111ll111l1_opy_
            webdriver.Remote.__init__ = bstack1l1111l11l_opy_
            if not isinstance(os.getenv(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫ⑌")), str):
                return
            WebDriver.quit = bstack11ll11lll1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1ll1ll11_opy_.on():
            webdriver.Remote.__init__ = bstack1l11111l1_opy_
        bstack1l1111ll11_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11l11ll_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩ⑍")):
        bstack1l1111ll11_opy_ = eval(os.environ.get(bstack11l11ll_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪ⑎")))
    if not bstack1l1111ll11_opy_:
        bstack1111lllll1_opy_(bstack11l11ll_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣ⑏"), bstack1ll11lll11_opy_)
    if bstack11ll1l11l1_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11l11ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ⑐")) and callable(getattr(RemoteConnection, bstack11l11ll_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⑑"))):
                RemoteConnection._get_proxy_url = bstack1l11l1lll_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack1l11l1lll_opy_
        except Exception as e:
            logger.error(bstack11l1l1ll11_opy_.format(str(e)))
    if bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ⑒") in str(framework_name).lower():
        if not bstack1lll1l11l11_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1111l1lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1lll1lllll_opy_
            Config.getoption = bstack111111lll_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack111l1ll11l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1llll111ll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_, bstack1lll1ll1ll_opy_=bstack1l1l1l1ll1_opy_)
def bstack11ll11lll1_opy_(self):
    global bstack1ll11l111l_opy_
    global bstack11l111l1ll_opy_
    global bstack1l1llll1l_opy_
    try:
        if bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⑓") in bstack1ll11l111l_opy_ and self.session_id != None and bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨ⑔"), bstack11l11ll_opy_ (u"ࠬ࠭⑕")) != bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⑖"):
            bstack11l111111l_opy_ = bstack11l11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⑗") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⑘")
            bstack1l1ll1l1l_opy_(logger, True)
            if os.environ.get(bstack11l11ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ⑙"), None):
                self.execute_script(
                    bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ⑚") + json.dumps(
                        os.environ.get(bstack11l11ll_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ⑛"))) + bstack11l11ll_opy_ (u"ࠬࢃࡽࠨ⑜"))
            if self != None:
                bstack111l1l11l1_opy_(self, bstack11l111111l_opy_, bstack11l11ll_opy_ (u"࠭ࠬࠡࠩ⑝").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l11l1l1l_opy_(bstack1l1l1ll1l1l_opy_):
            item = store.get(bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⑞"), None)
            if item is not None and bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ⑟"), None):
                bstack1llll1lll_opy_.bstack111l11l1_opy_(self, bstack11111ll1l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11l11ll_opy_ (u"ࠩࠪ①")
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦ②") + str(e))
    bstack1l1llll1l_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack11l1l1llll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_, bstack1lll1ll1ll_opy_=bstack1l1l1l1ll1_opy_)
def bstack1l1111l11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11l111l1ll_opy_
    global bstack1l1l1l1ll1_opy_
    global bstack1llll1lll1_opy_
    global bstack1ll11l111l_opy_
    global bstack1l11111ll_opy_
    global bstack1l1l1l111l_opy_
    global bstack11l1l1111_opy_
    global bstack11lllll1ll_opy_
    global bstack11111ll1l1_opy_
    CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭③")] = str(bstack1ll11l111l_opy_) + str(__version__)
    command_executor = bstack1111l1111l_opy_(bstack11l1l1111_opy_, CONFIG)
    logger.debug(bstack111l111111_opy_.format(command_executor))
    proxy = bstack11l11lllll_opy_(CONFIG, proxy)
    bstack11lll1ll11_opy_ = 0
    try:
        if bstack1llll1lll1_opy_ is True:
            bstack11lll1ll11_opy_ = int(os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ④")))
    except:
        bstack11lll1ll11_opy_ = 0
    bstack11ll1llll_opy_ = bstack11111ll1ll_opy_(CONFIG, bstack11lll1ll11_opy_)
    logger.debug(bstack1ll1ll111l_opy_.format(str(bstack11ll1llll_opy_)))
    bstack11111ll1l1_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⑤"))[bstack11lll1ll11_opy_]
    if bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ⑥") in CONFIG and CONFIG[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ⑦")]:
        bstack1ll1l111l_opy_(bstack11ll1llll_opy_, bstack11lllll1ll_opy_)
    if bstack111l1ll1_opy_.bstack1ll11ll1l1_opy_(CONFIG, bstack11lll1ll11_opy_) and bstack111l1ll1_opy_.bstack11llll1ll_opy_(bstack11ll1llll_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l11l1l1l_opy_(bstack1l1l1ll1l1l_opy_):
            bstack111l1ll1_opy_.set_capabilities(bstack11ll1llll_opy_, CONFIG)
    if desired_capabilities:
        bstack11l11lll11_opy_ = bstack1lll11111l_opy_(desired_capabilities)
        bstack11l11lll11_opy_[bstack11l11ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ⑧")] = bstack1lllll1ll1_opy_(CONFIG)
        bstack111l11ll11_opy_ = bstack11111ll1ll_opy_(bstack11l11lll11_opy_)
        if bstack111l11ll11_opy_:
            bstack11ll1llll_opy_ = update(bstack111l11ll11_opy_, bstack11ll1llll_opy_)
        desired_capabilities = None
    if options:
        bstack11ll1l11l_opy_(options, bstack11ll1llll_opy_)
    if not options:
        options = bstack1111l111l1_opy_(bstack11ll1llll_opy_)
    if proxy and bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ⑨")):
        options.proxy(proxy)
    if options and bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ⑩")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11l11l111_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ⑪")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11ll1llll_opy_)
    logger.info(bstack1l11l11l1l_opy_)
    bstack1l111l1l1_opy_.end(EVENTS.bstack1ll111111_opy_.value, EVENTS.bstack1ll111111_opy_.value + bstack11l11ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⑫"),
                               EVENTS.bstack1ll111111_opy_.value + bstack11l11ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ⑬"), True, None)
    try:
        if bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ⑭")):
            bstack1l11111ll_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ⑮")):
            bstack1l11111ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪ⑯")):
            bstack1l11111ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1l11111ll_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack1111l1l1l_opy_:
        logger.error(bstack1l1ll111l1_opy_.format(bstack11l11ll_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠪ⑰"), str(bstack1111l1l1l_opy_)))
        raise bstack1111l1l1l_opy_
    try:
        bstack1ll1ll1l1_opy_ = bstack11l11ll_opy_ (u"ࠬ࠭⑱")
        if bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ⑲")):
            bstack1ll1ll1l1_opy_ = self.caps.get(bstack11l11ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ⑳"))
        else:
            bstack1ll1ll1l1_opy_ = self.capabilities.get(bstack11l11ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ⑴"))
        if bstack1ll1ll1l1_opy_:
            bstack11l1111ll_opy_(bstack1ll1ll1l1_opy_)
            if bstack11l11l111_opy_() <= version.parse(bstack11l11ll_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ⑵")):
                self.command_executor._url = bstack11l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ⑶") + bstack11l1l1111_opy_ + bstack11l11ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ⑷")
            else:
                self.command_executor._url = bstack11l11ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ⑸") + bstack1ll1ll1l1_opy_ + bstack11l11ll_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢ⑹")
            logger.debug(bstack111l1l1l1l_opy_.format(bstack1ll1ll1l1_opy_))
        else:
            logger.debug(bstack1l1lll11l_opy_.format(bstack11l11ll_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣ⑺")))
    except Exception as e:
        logger.debug(bstack1l1lll11l_opy_.format(e))
    bstack11l111l1ll_opy_ = self.session_id
    if bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ⑻") in bstack1ll11l111l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11l11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭⑼"), None)
        if item:
            bstack1lll1ll11lll_opy_ = getattr(item, bstack11l11ll_opy_ (u"ࠪࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨ⑽"), False)
            if not getattr(item, bstack11l11ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⑾"), None) and bstack1lll1ll11lll_opy_:
                setattr(store[bstack11l11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⑿")], bstack11l11ll_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧ⒀"), self)
        bstack1l11l1llll_opy_ = getattr(threading.current_thread(), bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨ⒁"), None)
        if bstack1l11l1llll_opy_ and bstack1l11l1llll_opy_.get(bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⒂"), bstack11l11ll_opy_ (u"ࠩࠪ⒃")) == bstack11l11ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⒄"):
            bstack1ll1ll11_opy_.bstack1l111lll1l_opy_(self)
    bstack1l1l1l111l_opy_.append(self)
    if bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⒅") in CONFIG and bstack11l11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⒆") in CONFIG[bstack11l11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⒇")][bstack11lll1ll11_opy_]:
        bstack1l1l1l1ll1_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⒈")][bstack11lll1ll11_opy_][bstack11l11ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⒉")]
    logger.debug(bstack1l1l11l111_opy_.format(bstack11l111l1ll_opy_))
@measure(event_name=EVENTS.bstack1l111l1ll1_opy_, stage=STAGE.bstack1l1l1l1lll_opy_, bstack1lll1ll1ll_opy_=bstack1l1l1l1ll1_opy_)
def bstack111ll111l1_opy_(self, url):
    global bstack111lllll1_opy_
    global CONFIG
    try:
        bstack1l111l1lll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll11111l_opy_.format(str(err)))
    try:
        bstack111lllll1_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1ll11111ll_opy_):
                bstack1l111l1lll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll11111l_opy_.format(str(err)))
        raise e
def bstack11l11l1l1l_opy_(item, when):
    global bstack111l111l1l_opy_
    try:
        bstack111l111l1l_opy_(item, when)
    except Exception as e:
        pass
def bstack111l1ll11l_opy_(item, call, rep):
    global bstack111l11111_opy_
    global bstack1l1l1l111l_opy_
    name = bstack11l11ll_opy_ (u"ࠩࠪ⒊")
    try:
        if rep.when == bstack11l11ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ⒋"):
            bstack11l111l1ll_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⒌"))
            try:
                if (str(skipSessionName).lower() != bstack11l11ll_opy_ (u"ࠬࡺࡲࡶࡧࠪ⒍")):
                    name = str(rep.nodeid)
                    bstack11ll11l111_opy_ = bstack1l111111l1_opy_(bstack11l11ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⒎"), name, bstack11l11ll_opy_ (u"ࠧࠨ⒏"), bstack11l11ll_opy_ (u"ࠨࠩ⒐"), bstack11l11ll_opy_ (u"ࠩࠪ⒑"), bstack11l11ll_opy_ (u"ࠪࠫ⒒"))
                    os.environ[bstack11l11ll_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ⒓")] = name
                    for driver in bstack1l1l1l111l_opy_:
                        if bstack11l111l1ll_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll11l111_opy_)
            except Exception as e:
                logger.debug(bstack11l11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ⒔").format(str(e)))
            try:
                bstack11l1l1l11l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11l11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⒕"):
                    status = bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⒖") if rep.outcome.lower() == bstack11l11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⒗") else bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⒘")
                    reason = bstack11l11ll_opy_ (u"ࠪࠫ⒙")
                    if status == bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⒚"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ⒛") if status == bstack11l11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⒜") else bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⒝")
                    data = name + bstack11l11ll_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ⒞") if status == bstack11l11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⒟") else name + bstack11l11ll_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭⒠") + reason
                    bstack1llll111l1_opy_ = bstack1l111111l1_opy_(bstack11l11ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭⒡"), bstack11l11ll_opy_ (u"ࠬ࠭⒢"), bstack11l11ll_opy_ (u"࠭ࠧ⒣"), bstack11l11ll_opy_ (u"ࠧࠨ⒤"), level, data)
                    for driver in bstack1l1l1l111l_opy_:
                        if bstack11l111l1ll_opy_ == driver.session_id:
                            driver.execute_script(bstack1llll111l1_opy_)
            except Exception as e:
                logger.debug(bstack11l11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ⒥").format(str(e)))
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭⒦").format(str(e)))
    bstack111l11111_opy_(item, call, rep)
notset = Notset()
def bstack111111lll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l11l11ll_opy_
    if str(name).lower() == bstack11l11ll_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪ⒧"):
        return bstack11l11ll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ⒨")
    else:
        return bstack1l11l11ll_opy_(self, name, default, skip)
def bstack1l11l1lll_opy_(self):
    global CONFIG
    global bstack1llll11l1l_opy_
    try:
        proxy = bstack1l11ll111l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11l11ll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ⒩")):
                proxies = bstack111ll1ll1_opy_(proxy, bstack1111l1111l_opy_())
                if len(proxies) > 0:
                    protocol, bstack111l111l1_opy_ = proxies.popitem()
                    if bstack11l11ll_opy_ (u"ࠨ࠺࠰࠱ࠥ⒪") in bstack111l111l1_opy_:
                        return bstack111l111l1_opy_
                    else:
                        return bstack11l11ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ⒫") + bstack111l111l1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11l11ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧ⒬").format(str(e)))
    return bstack1llll11l1l_opy_(self)
def bstack11ll1l11l1_opy_():
    return (bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ⒭") in CONFIG or bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ⒮") in CONFIG) and bstack11lll11l1_opy_() and bstack11l11l111_opy_() >= version.parse(
        bstack1l1ll11111_opy_)
def bstack1l11lll1ll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1l1l1ll1_opy_
    global bstack1llll1lll1_opy_
    global bstack1ll11l111l_opy_
    CONFIG[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭⒯")] = str(bstack1ll11l111l_opy_) + str(__version__)
    bstack11lll1ll11_opy_ = 0
    try:
        if bstack1llll1lll1_opy_ is True:
            bstack11lll1ll11_opy_ = int(os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⒰")))
    except:
        bstack11lll1ll11_opy_ = 0
    CONFIG[bstack11l11ll_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ⒱")] = True
    bstack11ll1llll_opy_ = bstack11111ll1ll_opy_(CONFIG, bstack11lll1ll11_opy_)
    logger.debug(bstack1ll1ll111l_opy_.format(str(bstack11ll1llll_opy_)))
    if CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ⒲")):
        bstack1ll1l111l_opy_(bstack11ll1llll_opy_, bstack11lllll1ll_opy_)
    if bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⒳") in CONFIG and bstack11l11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⒴") in CONFIG[bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⒵")][bstack11lll1ll11_opy_]:
        bstack1l1l1l1ll1_opy_ = CONFIG[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧⒶ")][bstack11lll1ll11_opy_][bstack11l11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪⒷ")]
    import urllib
    import json
    if bstack11l11ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪⒸ") in CONFIG and str(CONFIG[bstack11l11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫⒹ")]).lower() != bstack11l11ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧⒺ"):
        bstack11l1ll111l_opy_ = bstack111l1l111_opy_()
        bstack11ll1lllll_opy_ = bstack11l1ll111l_opy_ + urllib.parse.quote(json.dumps(bstack11ll1llll_opy_))
    else:
        bstack11ll1lllll_opy_ = bstack11l11ll_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫⒻ") + urllib.parse.quote(json.dumps(bstack11ll1llll_opy_))
    browser = self.connect(bstack11ll1lllll_opy_)
    return browser
def bstack1111ll111_opy_():
    global bstack1l1111ll11_opy_
    global bstack1ll11l111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l1l11l11l_opy_
        if not bstack1lll1l11l11_opy_():
            global bstack1ll1ll1ll_opy_
            if not bstack1ll1ll1ll_opy_:
                from bstack_utils.helper import bstack1l11l1l11_opy_, bstack11111l1ll_opy_
                bstack1ll1ll1ll_opy_ = bstack1l11l1l11_opy_()
                bstack11111l1ll_opy_(bstack1ll11l111l_opy_)
            BrowserType.connect = bstack1l1l11l11l_opy_
            return
        BrowserType.launch = bstack1l11lll1ll_opy_
        bstack1l1111ll11_opy_ = True
    except Exception as e:
        pass
def bstack1lll1ll1111l_opy_():
    global CONFIG
    global bstack1l1llll1ll_opy_
    global bstack11l1l1111_opy_
    global bstack11lllll1ll_opy_
    global bstack1llll1lll1_opy_
    global bstack11lll1lll1_opy_
    CONFIG = json.loads(os.environ.get(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩⒼ")))
    bstack1l1llll1ll_opy_ = eval(os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬⒽ")))
    bstack11l1l1111_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬⒾ"))
    bstack1l1ll1l11l_opy_(CONFIG, bstack1l1llll1ll_opy_)
    bstack11lll1lll1_opy_ = bstack11l1l11ll1_opy_.configure_logger(CONFIG, bstack11lll1lll1_opy_)
    if cli.bstack1111l1ll1_opy_():
        bstack1lll1l1lll_opy_.invoke(Events.CONNECT, bstack1l1111ll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭Ⓙ"), bstack11l11ll_opy_ (u"ࠧ࠱ࠩⓀ")))
        cli.bstack1l1l1ll11ll_opy_(cli_context.platform_index)
        cli.bstack1l1l1llllll_opy_(bstack1111l1111l_opy_(bstack11l1l1111_opy_, CONFIG), cli_context.platform_index, bstack1111l111l1_opy_)
        cli.bstack1l1l1111lll_opy_()
        logger.debug(bstack11l11ll_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢⓁ") + str(cli_context.platform_index) + bstack11l11ll_opy_ (u"ࠤࠥⓂ"))
        return # skip all existing operations
    global bstack1l11111ll_opy_
    global bstack1l1llll1l_opy_
    global bstack1ll1l1lll_opy_
    global bstack11lll11ll1_opy_
    global bstack1111111ll_opy_
    global bstack11ll1ll1l1_opy_
    global bstack11llllll1l_opy_
    global bstack111lllll1_opy_
    global bstack1llll11l1l_opy_
    global bstack1l11l11ll_opy_
    global bstack111l111l1l_opy_
    global bstack111l11111_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l11111ll_opy_ = webdriver.Remote.__init__
        bstack1l1llll1l_opy_ = WebDriver.quit
        bstack11llllll1l_opy_ = WebDriver.close
        bstack111lllll1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ⓝ") in CONFIG or bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨⓄ") in CONFIG) and bstack11lll11l1_opy_():
        if bstack11l11l111_opy_() < version.parse(bstack1l1ll11111_opy_):
            logger.error(bstack11lll111l_opy_.format(bstack11l11l111_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11l11ll_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭Ⓟ")) and callable(getattr(RemoteConnection, bstack11l11ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧⓆ"))):
                    bstack1llll11l1l_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1llll11l1l_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack11l1l1ll11_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l11l11ll_opy_ = Config.getoption
        from _pytest import runner
        bstack111l111l1l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack111ll1ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack111l11111_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨⓇ"))
    bstack11lllll1ll_opy_ = CONFIG.get(bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬⓈ"), {}).get(bstack11l11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫⓉ"))
    bstack1llll1lll1_opy_ = True
    bstack1ll1l11l1l_opy_(bstack111ll11lll_opy_)
if (bstack1111l1lll11_opy_()):
    bstack1lll1ll1111l_opy_()
@error_handler(class_method=False)
def bstack1lll1lllll1l_opy_(hook_name, event, bstack1ll1l111ll1_opy_=None):
    if hook_name not in [bstack11l11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫⓊ"), bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨⓋ"), bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫⓌ"), bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨⓍ"), bstack11l11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬⓎ"), bstack11l11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩⓏ"), bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨⓐ"), bstack11l11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬⓑ")]:
        return
    node = store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨⓒ")]
    if hook_name in [bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫⓓ"), bstack11l11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨⓔ")]:
        node = store[bstack11l11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ⓕ")]
    elif hook_name in [bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ⓖ"), bstack11l11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪⓗ")]:
        node = store[bstack11l11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨⓘ")]
    hook_type = bstack11l111l1ll1_opy_(hook_name)
    if event == bstack11l11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫⓙ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_[hook_type], bstack1lll1l1llll_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1lll1ll1_opy_ = {
            bstack11l11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪⓚ"): uuid,
            bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪⓛ"): bstack1ll1ll1l_opy_(),
            bstack11l11ll_opy_ (u"ࠧࡵࡻࡳࡩࠬⓜ"): bstack11l11ll_opy_ (u"ࠨࡪࡲࡳࡰ࠭ⓝ"),
            bstack11l11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬⓞ"): hook_type,
            bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ⓟ"): hook_name
        }
        store[bstack11l11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨⓠ")].append(uuid)
        bstack1lll1lll1l1l_opy_ = node.nodeid
        if hook_type == bstack11l11ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪⓡ"):
            if not _1lll1l11_opy_.get(bstack1lll1lll1l1l_opy_, None):
                _1lll1l11_opy_[bstack1lll1lll1l1l_opy_] = {bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬⓢ"): []}
            _1lll1l11_opy_[bstack1lll1lll1l1l_opy_][bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ⓣ")].append(bstack1lll1ll1_opy_[bstack11l11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ⓤ")])
        _1lll1l11_opy_[bstack1lll1lll1l1l_opy_ + bstack11l11ll_opy_ (u"ࠩ࠰ࠫⓥ") + hook_name] = bstack1lll1ll1_opy_
        bstack1lll1ll1l1ll_opy_(node, bstack1lll1ll1_opy_, bstack11l11ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫⓦ"))
    elif event == bstack11l11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪⓧ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll11l1_opy_[hook_type], bstack1lll1l1llll_opy_.POST, node, None, bstack1ll1l111ll1_opy_)
            return
        bstack1ll1l1ll_opy_ = node.nodeid + bstack11l11ll_opy_ (u"ࠬ࠳ࠧⓨ") + hook_name
        _1lll1l11_opy_[bstack1ll1l1ll_opy_][bstack11l11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫⓩ")] = bstack1ll1ll1l_opy_()
        bstack1lll1lllll11_opy_(_1lll1l11_opy_[bstack1ll1l1ll_opy_][bstack11l11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⓪")])
        bstack1lll1ll1l1ll_opy_(node, _1lll1l11_opy_[bstack1ll1l1ll_opy_], bstack11l11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⓫"), bstack1lll1ll1l111_opy_=bstack1ll1l111ll1_opy_)
def bstack1lll1ll111ll_opy_():
    global bstack1lll1llll11l_opy_
    if bstack11ll1l1l1_opy_():
        bstack1lll1llll11l_opy_ = bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭⓬")
    else:
        bstack1lll1llll11l_opy_ = bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⓭")
@bstack1ll1ll11_opy_.bstack1llll11l11ll_opy_
def bstack1lll1llll111_opy_():
    bstack1lll1ll111ll_opy_()
    if cli.is_running():
        try:
            bstack11l1l1lllll_opy_(bstack1lll1lllll1l_opy_)
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧ⓮").format(e))
        return
    if bstack11lll11l1_opy_():
        bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
        bstack11l11ll_opy_ (u"ࠬ࠭ࠧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡆࡰࡴࠣࡴࡵࡶࠠ࠾ࠢ࠴࠰ࠥࡳ࡯ࡥࡡࡨࡼࡪࡩࡵࡵࡧࠣ࡫ࡪࡺࡳࠡࡷࡶࡩࡩࠦࡦࡰࡴࠣࡥ࠶࠷ࡹࠡࡥࡲࡱࡲࡧ࡮ࡥࡵ࠰ࡻࡷࡧࡰࡱ࡫ࡱ࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡱࡲࡳࠤࡃࠦ࠱࠭ࠢࡰࡳࡩࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡵࡹࡳࠦࡢࡦࡥࡤࡹࡸ࡫ࠠࡪࡶࠣ࡭ࡸࠦࡰࡢࡶࡦ࡬ࡪࡪࠠࡪࡰࠣࡥࠥࡪࡩࡧࡨࡨࡶࡪࡴࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࠢ࡬ࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭ࡻࡳࠡࡹࡨࠤࡳ࡫ࡥࡥࠢࡷࡳࠥࡻࡳࡦࠢࡖࡩࡱ࡫࡮ࡪࡷࡰࡔࡦࡺࡣࡩࠪࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠮ࠦࡦࡰࡴࠣࡴࡵࡶࠠ࠿ࠢ࠴ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ࠧࠨ⓯")
        if bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ⓰")):
            if CONFIG.get(bstack11l11ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ⓱")) is not None and int(CONFIG[bstack11l11ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⓲")]) > 1:
                bstack11l1lll1l1_opy_(bstack1ll1lll1ll_opy_)
            return
        bstack11l1lll1l1_opy_(bstack1ll1lll1ll_opy_)
    try:
        bstack11l1l1lllll_opy_(bstack1lll1lllll1l_opy_)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࡹࠠࡱࡣࡷࡧ࡭ࡀࠠࡼࡿࠥ⓳").format(e))
bstack1lll1llll111_opy_()