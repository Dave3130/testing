# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1ll11111ll_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l1111llll_opy_, bstack1111ll11l1_opy_, update, bstack1lllll11ll_opy_,
                                       bstack1llll1lll1_opy_, bstack1ll1l1l1l_opy_, bstack1l1ll11ll1_opy_, bstack11ll1l1ll1_opy_,
                                       bstack1l111l1ll1_opy_, bstack1l11l1l111_opy_, bstack11l1111l1l_opy_,
                                       bstack1l1l1l1111_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1l11l1l1ll_opy_)
from browserstack_sdk.bstack1lll1llll_opy_ import bstack1llllll1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack111111l11l_opy_
from bstack_utils.capture import bstack1l1l111l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1lllll1l11_opy_, bstack1111l11l11_opy_, bstack1l11ll111l_opy_, \
    bstack111llllll1_opy_
from bstack_utils.helper import bstack1lll1lll_opy_, bstack111l111llll_opy_, bstack1lll11ll_opy_, bstack11l111lll1_opy_, bstack1lll11ll11l_opy_, bstack1l1lll11_opy_, \
    bstack1111l11ll1l_opy_, \
    bstack111l1l1ll1l_opy_, bstack1l1llllll_opy_, bstack1111l1ll11_opy_, bstack111l1111ll1_opy_, bstack11l111ll1l_opy_, Notset, \
    bstack1l1lll1lll_opy_, bstack111l11ll111_opy_, bstack1111l1l1111_opy_, Result, bstack1111ll1l1ll_opy_, bstack1111l11l11l_opy_, error_handler, \
    bstack111lll11ll_opy_, bstack11ll1l1ll_opy_, bstack1l1111l1ll_opy_, bstack1111ll11l1l_opy_
from bstack_utils.bstack11l1l1l1ll1_opy_ import bstack11l1l1ll11l_opy_
from bstack_utils.messages import bstack1l1l11l111_opy_, bstack1l11l11111_opy_, bstack1111l1lll_opy_, bstack1lllllll1l_opy_, bstack11111lll_opy_, \
    bstack1l111l11ll_opy_, bstack1ll11l1l11_opy_, bstack11lll111l_opy_, bstack11ll11l1l1_opy_, bstack1l1ll1lll_opy_, \
    bstack1l111l1l1_opy_, bstack111l1l11ll_opy_, bstack1l1ll1l11l_opy_
from bstack_utils.proxy import bstack1lll11l11l_opy_, bstack1ll1ll11l1_opy_
from bstack_utils.bstack1l1111ll11_opy_ import bstack11l1111l111_opy_, bstack11l1111l11l_opy_, bstack11l1111l1ll_opy_, bstack11l111l11ll_opy_, \
    bstack11l1111l1l1_opy_, bstack11l111l1111_opy_, bstack11l1111ll1l_opy_, bstack1lll1lllll_opy_, bstack11l1111ll11_opy_
from bstack_utils.bstack1l111ll11_opy_ import bstack1lll11l111_opy_
from bstack_utils.bstack11111lll1_opy_ import bstack1l1111111l_opy_, bstack11ll11lll1_opy_, bstack111l1l11l1_opy_, \
    bstack11l1ll1111_opy_, bstack1111l1l11_opy_
from bstack_utils.bstack1ll1l11l_opy_ import bstack1l1llll1_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack1l11lll1_opy_
import bstack_utils.accessibility as bstack111111l1_opy_
from bstack_utils.bstack1l1l1l1l_opy_ import bstack11lllll1_opy_
from bstack_utils.bstack11l1lll1l_opy_ import bstack11l1lll1l_opy_
from bstack_utils.bstack1lll1ll11_opy_ import bstack111l11ll_opy_
from browserstack_sdk.__init__ import bstack1l1l1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l11lll11l1_opy_ import bstack1l1l11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack111llllll_opy_ import bstack111llllll_opy_, Events, bstack11l1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll1l11ll1l_opy_, bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack111llllll_opy_ import bstack111llllll_opy_, Events, bstack11l1l11l1_opy_
bstack1l1l11ll1l_opy_ = None
bstack1l111ll111_opy_ = None
bstack11ll11l11_opy_ = None
bstack11l1l1l111_opy_ = None
bstack1l11l1111_opy_ = None
bstack1lllllllll_opy_ = None
bstack11ll1ll1l1_opy_ = None
bstack11l11l1ll_opy_ = None
bstack111l1l111l_opy_ = None
bstack11lllll111_opy_ = None
bstack11l11ll1l1_opy_ = None
bstack11111ll1l_opy_ = None
bstack1l1l11l1ll_opy_ = None
bstack1111ll111l_opy_ = bstack11111_opy_ (u"ࠪࠫ⊨")
CONFIG = {}
bstack11l11l1111_opy_ = False
bstack111l11111l_opy_ = bstack11111_opy_ (u"ࠫࠬ⊩")
bstack1ll111l11l_opy_ = bstack11111_opy_ (u"ࠬ࠭⊪")
bstack1l11lll111_opy_ = False
bstack11ll11l1ll_opy_ = []
bstack1l1lll1l1_opy_ = bstack1lllll1l11_opy_
bstack1lll1lll1lll_opy_ = bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⊫")
bstack1ll1l11l11_opy_ = {}
bstack11ll11111_opy_ = None
bstack1l111111l_opy_ = False
logger = bstack111111l11l_opy_.get_logger(__name__, bstack1l1lll1l1_opy_)
store = {
    bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⊬"): []
}
bstack1lll1ll1l1ll_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11llll1l_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll1l11ll1l_opy_(
    test_framework_name=bstack111ll11ll_opy_[bstack11111_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈࠬ⊭")] if bstack11l111ll1l_opy_() else bstack111ll11ll_opy_[bstack11111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩ⊮")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack11ll1111l1_opy_(page, bstack1l1l11lll_opy_):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ⊯"),
                      bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ⊰") + json.dumps(
                          bstack1l1l11lll_opy_) + bstack11111_opy_ (u"ࠧࢃࡽࠣ⊱"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦ⊲"), e)
def bstack11111lll11_opy_(page, message, level):
    try:
        page.evaluate(bstack11111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ⊳"), bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭⊴") + json.dumps(
            message) + bstack11111_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬ⊵") + json.dumps(level) + bstack11111_opy_ (u"ࠪࢁࢂ࠭⊶"))
    except Exception as e:
        print(bstack11111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢ⊷"), e)
def pytest_configure(config):
    global bstack111l11111l_opy_
    global CONFIG
    bstack111lll11_opy_ = Config.bstack1111llll_opy_()
    config.args = bstack1l11lll1_opy_.bstack11l111ll1ll_opy_(config.args)
    bstack111lll11_opy_.bstack111l11lll_opy_(bstack1l1111l1ll_opy_(config.getoption(bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ⊸"))))
    try:
        bstack111111l11l_opy_.bstack111111ll111_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack111llllll_opy_.invoke(Events.CONNECT, bstack11l1l11l1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⊹"), bstack11111_opy_ (u"ࠧ࠱ࠩ⊺")))
        config = json.loads(os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢ⊻"), bstack11111_opy_ (u"ࠤࡾࢁࠧ⊼")))
        cli.bstack1l1l1l1l111_opy_(bstack1111l1ll11_opy_(bstack111l11111l_opy_, CONFIG), cli_context.platform_index, bstack1lllll11ll_opy_)
    if cli.bstack1l1l1l1l1l1_opy_(bstack1l1l11l11l1_opy_):
        cli.bstack1l1l1l111ll_opy_()
        logger.debug(bstack11111_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤ⊽") + str(cli_context.platform_index) + bstack11111_opy_ (u"ࠦࠧ⊾"))
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_ALL, bstack1lll1ll1l1l_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11111_opy_ (u"ࠧࡽࡨࡦࡰࠥ⊿"), None)
    if cli.is_running() and when == bstack11111_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ⋀"):
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG_REPORT, bstack1lll1ll1l1l_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11111_opy_ (u"ࠢࡤࡣ࡯ࡰࠧ⋁"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⋂")))
        if not passed:
            config = json.loads(os.environ.get(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠣ⋃"), bstack11111_opy_ (u"ࠥࡿࢂࠨ⋄")))
            if bstack111l11ll_opy_.bstack111l1111_opy_(config):
                bstack1lllll1lll1l_opy_ = bstack111l11ll_opy_.bstack1lllll1l1_opy_(config)
                if item.execution_count > bstack1lllll1lll1l_opy_:
                    print(bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡴࡨࡸࡷ࡯ࡥࡴ࠼ࠣࠫ⋅"), report.nodeid, os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ⋆")))
                    bstack111l11ll_opy_.bstack111llll1l1l_opy_(report.nodeid)
            else:
                print(bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥ࠭⋇"), report.nodeid, os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⋈")))
                bstack111l11ll_opy_.bstack111llll1l1l_opy_(report.nodeid)
        else:
            print(bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࠦࡰࡢࡵࡶࡩࡩࡀࠠࠨ⋉"), report.nodeid, os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⋊")))
    if cli.is_running():
        if when == bstack11111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ⋋"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1ll1l1l_opy_.POST, item, call, outcome)
        elif when == bstack11111_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ⋌"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG_REPORT, bstack1lll1ll1l1l_opy_.POST, item, call, outcome)
        elif when == bstack11111_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ⋍"):
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.AFTER_EACH, bstack1lll1ll1l1l_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11111_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⋎"))
    plugins = item.config.getoption(bstack11111_opy_ (u"ࠢࡱ࡮ࡸ࡫࡮ࡴࡳࠣ⋏"))
    report = outcome.get_result()
    os.environ[bstack11111_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ⋐")] = report.nodeid
    bstack1lll1ll11ll1_opy_(item, call, report)
    if bstack11111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠢ⋑") not in plugins or bstack11l111ll1l_opy_():
        return
    summary = []
    driver = getattr(item, bstack11111_opy_ (u"ࠥࡣࡩࡸࡩࡷࡧࡵࠦ⋒"), None)
    page = getattr(item, bstack11111_opy_ (u"ࠦࡤࡶࡡࡨࡧࠥ⋓"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1ll1llll_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1llll11l_opy_(item, report, summary, skipSessionName)
def bstack1lll1ll1llll_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⋔") and report.skipped:
        bstack11l1111ll11_opy_(report)
    if report.when in [bstack11111_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧ⋕"), bstack11111_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ⋖")]:
        return
    if not bstack1lll11ll11l_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11111_opy_ (u"ࠨࡶࡵࡹࡪ࠭⋗")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ⋘") + json.dumps(
                    report.nodeid) + bstack11111_opy_ (u"ࠪࢁࢂ࠭⋙"))
        os.environ[bstack11111_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ⋚")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11111_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫࠺ࠡࡽ࠳ࢁࠧ⋛").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ⋜")))
    bstack1ll11ll11l_opy_ = bstack11111_opy_ (u"ࠢࠣ⋝")
    bstack11l1111ll11_opy_(report)
    if not passed:
        try:
            bstack1ll11ll11l_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11111_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣ⋞").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11ll11l_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ⋟")))
        bstack1ll11ll11l_opy_ = bstack11111_opy_ (u"ࠥࠦ⋠")
        if not passed:
            try:
                bstack1ll11ll11l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦ⋡").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll11ll11l_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩ⋢")
                    + json.dumps(bstack11111_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠧࠢ⋣"))
                    + bstack11111_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥ⋤")
                )
            else:
                item._driver.execute_script(
                    bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭⋥")
                    + json.dumps(str(bstack1ll11ll11l_opy_))
                    + bstack11111_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧ⋦")
                )
        except Exception as e:
            summary.append(bstack11111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡣࡱࡲࡴࡺࡡࡵࡧ࠽ࠤࢀ࠶ࡽࠣ⋧").format(e))
def bstack1lll1lll1ll1_opy_(test_name, error_message):
    try:
        bstack1lll1lll11ll_opy_ = []
        bstack11ll11lll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⋨"), bstack11111_opy_ (u"ࠬ࠶ࠧ⋩"))
        bstack111111lll_opy_ = {bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⋪"): test_name, bstack11111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⋫"): error_message, bstack11111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ⋬"): bstack11ll11lll_opy_}
        bstack1lll1ll1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ⋭"))
        if os.path.exists(bstack1lll1ll1l111_opy_):
            with open(bstack1lll1ll1l111_opy_) as f:
                bstack1lll1lll11ll_opy_ = json.load(f)
        bstack1lll1lll11ll_opy_.append(bstack111111lll_opy_)
        with open(bstack1lll1ll1l111_opy_, bstack11111_opy_ (u"ࠪࡻࠬ⋮")) as f:
            json.dump(bstack1lll1lll11ll_opy_, f)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡦࡴࡶ࡭ࡸࡺࡩ࡯ࡩࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡱࡻࡷࡩࡸࡺࠠࡦࡴࡵࡳࡷࡹ࠺ࠡࠩ⋯") + str(e))
def bstack1lll1llll11l_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11111_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ⋰"), bstack11111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ⋱")]:
        return
    if (str(skipSessionName).lower() != bstack11111_opy_ (u"ࠧࡵࡴࡸࡩࠬ⋲")):
        bstack11ll1111l1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⋳")))
    bstack1ll11ll11l_opy_ = bstack11111_opy_ (u"ࠤࠥ⋴")
    bstack11l1111ll11_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll11ll11l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11111_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ⋵").format(e)
                )
        try:
            if passed:
                bstack1111l1l11_opy_(getattr(item, bstack11111_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪ⋶"), None), bstack11111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ⋷"))
            else:
                error_message = bstack11111_opy_ (u"࠭ࠧ⋸")
                if bstack1ll11ll11l_opy_:
                    bstack11111lll11_opy_(item._page, str(bstack1ll11ll11l_opy_), bstack11111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ⋹"))
                    bstack1111l1l11_opy_(getattr(item, bstack11111_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧ⋺"), None), bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ⋻"), str(bstack1ll11ll11l_opy_))
                    error_message = str(bstack1ll11ll11l_opy_)
                else:
                    bstack1111l1l11_opy_(getattr(item, bstack11111_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⋼"), None), bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ⋽"))
                bstack1lll1lll1ll1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11111_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁ࠰ࡾࠤ⋾").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11111_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ⋿"), default=bstack11111_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨ⌀"), help=bstack11111_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢ⌁"))
    parser.addoption(bstack11111_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ⌂"), default=bstack11111_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤ⌃"), help=bstack11111_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥ⌄"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11111_opy_ (u"ࠧ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠢ⌅"), action=bstack11111_opy_ (u"ࠨࡳࡵࡱࡵࡩࠧ⌆"), default=bstack11111_opy_ (u"ࠢࡤࡪࡵࡳࡲ࡫ࠢ⌇"),
                         help=bstack11111_opy_ (u"ࠣࡆࡵ࡭ࡻ࡫ࡲࠡࡶࡲࠤࡷࡻ࡮ࠡࡶࡨࡷࡹࡹࠢ⌈"))
def bstack1l1l11l1_opy_(log):
    if not (log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⌉")] and log[bstack11111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⌊")].strip()):
        return
    active = bstack11lll11l_opy_()
    log = {
        bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⌋"): log[bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⌌")],
        bstack11111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⌍"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"࡛ࠧࠩ⌎"),
        bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⌏"): log[bstack11111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⌐")],
    }
    if active:
        if active[bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ⌑")] == bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⌒"):
            log[bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⌓")] = active[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⌔")]
        elif active[bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬ⌕")] == bstack11111_opy_ (u"ࠨࡶࡨࡷࡹ࠭⌖"):
            log[bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⌗")] = active[bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⌘")]
    bstack11lllll1_opy_.bstack1l11l1ll_opy_([log])
def bstack11lll11l_opy_():
    if len(store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⌙")]) > 0 and store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⌚")][-1]:
        return {
            bstack11111_opy_ (u"࠭ࡴࡺࡲࡨࠫ⌛"): bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ⌜"),
            bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⌝"): store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⌞")][-1]
        }
    if store.get(bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⌟"), None):
        return {
            bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩ⌠"): bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࠪ⌡"),
            bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⌢"): store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⌣")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.INIT_TEST, bstack1lll1ll1l1l_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.INIT_TEST, bstack1lll1ll1l1l_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1ll1111l_opy_ = True
        bstack11l11111ll_opy_ = bstack111111l1_opy_.bstack1llll1ll11_opy_(bstack111l1l1ll1l_opy_(item.own_markers))
        if not cli.bstack1l1l1l1l1l1_opy_(bstack1l1l11l11l1_opy_):
            item._a11y_test_case = bstack11l11111ll_opy_
            if bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ⌤"), None):
                driver = getattr(item, bstack11111_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⌥"), None)
                item._a11y_started = bstack111111l1_opy_.bstack11l1lll11_opy_(driver, bstack11l11111ll_opy_)
        if not bstack11lllll1_opy_.on() or bstack1lll1lll1lll_opy_ != bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⌦"):
            return
        global current_test_uuid #, bstack1l11l111_opy_
        bstack11llllll_opy_ = {
            bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩ⌧"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⌨"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"࡚࠭ࠨ〈")
        }
        current_test_uuid = bstack11llllll_opy_[bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ〉")]
        store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⌫")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌬")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11llll1l_opy_[item.nodeid] = {**_11llll1l_opy_[item.nodeid], **bstack11llllll_opy_}
        bstack1lll1ll1l11l_opy_(item, _11llll1l_opy_[item.nodeid], bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⌭"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡨࡧ࡬࡭࠼ࠣࡿࢂ࠭⌮"), str(err))
def pytest_runtest_setup(item):
    store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⌯")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1ll1l1l_opy_.PRE, item, bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⌰"))
    if bstack111l11ll_opy_.bstack11l11111ll1_opy_():
            bstack1lll1ll1ll1l_opy_ = bstack11111_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡢࡵࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦ⌱")
            logger.error(bstack1lll1ll1ll1l_opy_)
            bstack11llllll_opy_ = {
                bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⌲"): uuid4().__str__(),
                bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⌳"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"ࠪ࡞ࠬ⌴"),
                bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⌵"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"ࠬࡠࠧ⌶"),
                bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⌷"): bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⌸"),
                bstack11111_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ⌹"): bstack1lll1ll1ll1l_opy_,
                bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⌺"): [],
                bstack11111_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⌻"): []
            }
            bstack1lll1ll1l11l_opy_(item, bstack11llllll_opy_, bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⌼"))
            pytest.skip(bstack1lll1ll1ll1l_opy_)
            return # skip all existing operations
    global bstack1lll1ll1l1ll_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l1111ll1_opy_():
        atexit.register(bstack11l1l1111l_opy_)
        if not bstack1lll1ll1l1ll_opy_:
            try:
                bstack1lll1lll111l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack1111ll11l1l_opy_():
                    bstack1lll1lll111l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1lll111l_opy_:
                    signal.signal(s, bstack1lll1ll111l1_opy_)
                bstack1lll1ll1l1ll_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡪ࡭ࡸࡺࡥࡳࠢࡶ࡭࡬ࡴࡡ࡭ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࡶ࠾ࠥࠨ⌽") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l1111l111_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⌾")
    try:
        if not bstack11lllll1_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack11llllll_opy_ = {
            bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⌿"): uuid,
            bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍀"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"ࠩ࡝ࠫ⍁"),
            bstack11111_opy_ (u"ࠪࡸࡾࡶࡥࠨ⍂"): bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⍃"),
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⍄"): bstack11111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ⍅"),
            bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ⍆"): bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⍇")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭⍈")] = item
        store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⍉")] = [uuid]
        if not _11llll1l_opy_.get(item.nodeid, None):
            _11llll1l_opy_[item.nodeid] = {bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⍊"): [], bstack11111_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⍋"): []}
        _11llll1l_opy_[item.nodeid][bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⍌")].append(bstack11llllll_opy_[bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍍")])
        _11llll1l_opy_[item.nodeid + bstack11111_opy_ (u"ࠨ࠯ࡶࡩࡹࡻࡰࠨ⍎")] = bstack11llllll_opy_
        bstack1lll1l1lllll_opy_(item, bstack11llllll_opy_, bstack11111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⍏"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡷࡪࡺࡵࡱ࠼ࠣࡿࢂ࠭⍐"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.AFTER_EACH, bstack1lll1ll1l1l_opy_.PRE, item, bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⍑"))
        return # skip all existing operations
    try:
        global bstack1ll1l11l11_opy_
        bstack11ll11lll_opy_ = 0
        if bstack1l11lll111_opy_ is True:
            bstack11ll11lll_opy_ = int(os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⍒")))
        if bstack111ll1lll1_opy_.bstack11l1l1l1l1_opy_() == bstack11111_opy_ (u"ࠨࡴࡳࡷࡨࠦ⍓"):
            if bstack111ll1lll1_opy_.bstack1l1l1l1l1_opy_() == bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ⍔"):
                bstack1lll1ll111ll_opy_ = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⍕"), None)
                bstack1l1111ll1_opy_ = bstack1lll1ll111ll_opy_ + bstack11111_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧ⍖")
                driver = getattr(item, bstack11111_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ⍗"), None)
                bstack1l1lll11l1_opy_ = getattr(item, bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⍘"), None)
                bstack11l1ll1l11_opy_ = getattr(item, bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⍙"), None)
                PercySDK.screenshot(driver, bstack1l1111ll1_opy_, bstack1l1lll11l1_opy_=bstack1l1lll11l1_opy_, bstack11l1ll1l11_opy_=bstack11l1ll1l11_opy_, bstack1ll11l111l_opy_=bstack11ll11lll_opy_)
        if not cli.bstack1l1l1l1l1l1_opy_(bstack1l1l11l11l1_opy_):
            if getattr(item, bstack11111_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡢࡴࡷࡩࡩ࠭⍚"), False):
                bstack1llllll1l_opy_.bstack1lll11ll1_opy_(getattr(item, bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⍛"), None), bstack1ll1l11l11_opy_, logger, item)
        if not bstack11lllll1_opy_.on():
            return
        bstack11llllll_opy_ = {
            bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⍜"): uuid4().__str__(),
            bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⍝"): bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"ࠪ࡞ࠬ⍞"),
            bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩ⍟"): bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⍠"),
            bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⍡"): bstack11111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ⍢"),
            bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ⍣"): bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ⍤")
        }
        _11llll1l_opy_[item.nodeid + bstack11111_opy_ (u"ࠪ࠱ࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⍥")] = bstack11llllll_opy_
        bstack1lll1l1lllll_opy_(item, bstack11llllll_opy_, bstack11111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⍦"))
    except Exception as err:
        print(bstack11111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࠺ࠡࡽࢀࠫ⍧"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111l11ll_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬ⍨")] = request.node
    elif bstack11l1111l1l1_opy_(fixturedef.argname):
        store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬ⍩")] = request.node
    if not bstack11lllll1_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1ll1l1l_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1ll1l1l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1ll1l1l_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.SETUP_FIXTURE, bstack1lll1ll1l1l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭⍪"): fixturedef.argname,
            bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⍫"): bstack1111l11ll1l_opy_(outcome),
            bstack11111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⍬"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⍭")]
        if not _11llll1l_opy_.get(current_test_item.nodeid, None):
            _11llll1l_opy_[current_test_item.nodeid] = {bstack11111_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⍮"): []}
        _11llll1l_opy_[current_test_item.nodeid][bstack11111_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⍯")].append(fixture)
    except Exception as err:
        logger.debug(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡴࡧࡷࡹࡵࡀࠠࡼࡿࠪ⍰"), str(err))
if bstack11l111ll1l_opy_() and bstack11lllll1_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1ll1l1l_opy_.PRE, request, step)
            return
        try:
            _11llll1l_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⍱")].bstack11l1l11l_opy_(id(step))
        except Exception as err:
            print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲ࠽ࠤࢀࢃࠧ⍲"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1ll1l1l_opy_.POST, request, step, exception)
            return
        try:
            _11llll1l_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍳")].bstack1llll1ll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ⍴"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.STEP, bstack1lll1ll1l1l_opy_.POST, request, step)
            return
        try:
            bstack1ll1l11l_opy_: bstack1l1llll1_opy_ = _11llll1l_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⍵")]
            bstack1ll1l11l_opy_.bstack1llll1ll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪ⍶"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1lll1lll_opy_
        try:
            if not bstack11lllll1_opy_.on() or bstack1lll1lll1lll_opy_ != bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⍷"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.TEST, bstack1lll1ll1l1l_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ⍸"), None)
            if not _11llll1l_opy_.get(request.node.nodeid, None):
                _11llll1l_opy_[request.node.nodeid] = {}
            bstack1ll1l11l_opy_ = bstack1l1llll1_opy_.bstack111111l1l1l_opy_(
                scenario, feature, request.node,
                name=bstack11l111l1111_opy_(request.node, scenario),
                started_at=bstack1l1lll11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ⍹"),
                tags=bstack11l1111ll1l_opy_(feature, scenario),
                bstack1ll11111_opy_=bstack11lllll1_opy_.bstack1lll1ll1_opy_(driver) if driver and driver.session_id else {}
            )
            _11llll1l_opy_[request.node.nodeid][bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍺")] = bstack1ll1l11l_opy_
            bstack1lll1ll1lll1_opy_(bstack1ll1l11l_opy_.uuid)
            bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⍻"), bstack1ll1l11l_opy_)
        except Exception as err:
            print(bstack11111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ⍼"), str(err))
def bstack1lll1ll11l11_opy_(bstack11l11ll1_opy_):
    if bstack11l11ll1_opy_ in store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⍽")]:
        store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⍾")].remove(bstack11l11ll1_opy_)
def bstack1lll1ll1lll1_opy_(test_uuid):
    store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⍿")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack11lllll1_opy_.bstack1llll11l11ll_opy_
def bstack1lll1ll11ll1_opy_(item, call, report):
    logger.debug(bstack11111_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡴࡷࠫ⎀"))
    global bstack1lll1lll1lll_opy_
    bstack1lll1l1111_opy_ = bstack1l1lll11_opy_()
    if hasattr(report, bstack11111_opy_ (u"ࠪࡷࡹࡵࡰࠨ⎁")):
        bstack1lll1l1111_opy_ = bstack1111ll1l1ll_opy_(report.stop)
    elif hasattr(report, bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪ⎂")):
        bstack1lll1l1111_opy_ = bstack1111ll1l1ll_opy_(report.start)
    try:
        if getattr(report, bstack11111_opy_ (u"ࠬࡽࡨࡦࡰࠪ⎃"), bstack11111_opy_ (u"࠭ࠧ⎄")) == bstack11111_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ⎅"):
            logger.debug(bstack11111_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡵࡧࠣ࠱ࠥࢁࡽ࠭ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࠳ࠠࡼࡿࠪ⎆").format(getattr(report, bstack11111_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⎇"), bstack11111_opy_ (u"ࠪࠫ⎈")).__str__(), bstack1lll1lll1lll_opy_))
            if bstack1lll1lll1lll_opy_ == bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⎉"):
                _11llll1l_opy_[item.nodeid][bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎊")] = bstack1lll1l1111_opy_
                bstack1lll1ll1l11l_opy_(item, _11llll1l_opy_[item.nodeid], bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⎋"), report, call)
                store[bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⎌")] = None
            elif bstack1lll1lll1lll_opy_ == bstack11111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ⎍"):
                bstack1ll1l11l_opy_ = _11llll1l_opy_[item.nodeid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⎎")]
                bstack1ll1l11l_opy_.set(hooks=_11llll1l_opy_[item.nodeid].get(bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎏"), []))
                exception, bstack1l11l11l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11l11l_opy_ = [call.excinfo.exconly(), getattr(report, bstack11111_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪ⎐"), bstack11111_opy_ (u"ࠬ࠭⎑"))]
                bstack1ll1l11l_opy_.stop(time=bstack1lll1l1111_opy_, result=Result(result=getattr(report, bstack11111_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ⎒"), bstack11111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⎓")), exception=exception, bstack1l11l11l_opy_=bstack1l11l11l_opy_))
                bstack11lllll1_opy_.bstack1l1l11ll_opy_(bstack11111_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⎔"), _11llll1l_opy_[item.nodeid][bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⎕")])
        elif getattr(report, bstack11111_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⎖"), bstack11111_opy_ (u"ࠫࠬ⎗")) in [bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⎘"), bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⎙")]:
            logger.debug(bstack11111_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡴࡦࠢ࠰ࠤࢀࢃࠬࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࠲ࠦࡻࡾࠩ⎚").format(getattr(report, bstack11111_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⎛"), bstack11111_opy_ (u"ࠩࠪ⎜")).__str__(), bstack1lll1lll1lll_opy_))
            bstack1ll11ll1_opy_ = item.nodeid + bstack11111_opy_ (u"ࠪ࠱ࠬ⎝") + getattr(report, bstack11111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⎞"), bstack11111_opy_ (u"ࠬ࠭⎟"))
            if getattr(report, bstack11111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⎠"), False):
                hook_type = bstack11111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ⎡") if getattr(report, bstack11111_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⎢"), bstack11111_opy_ (u"ࠩࠪ⎣")) == bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⎤") else bstack11111_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨ⎥")
                _11llll1l_opy_[bstack1ll11ll1_opy_] = {
                    bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⎦"): uuid4().__str__(),
                    bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⎧"): bstack1lll1l1111_opy_,
                    bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⎨"): hook_type
                }
            _11llll1l_opy_[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎩")] = bstack1lll1l1111_opy_
            bstack1lll1ll11l11_opy_(_11llll1l_opy_[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⎪")])
            bstack1lll1l1lllll_opy_(item, _11llll1l_opy_[bstack1ll11ll1_opy_], bstack11111_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⎫"), report, call)
            if getattr(report, bstack11111_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⎬"), bstack11111_opy_ (u"ࠬ࠭⎭")) == bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⎮"):
                if getattr(report, bstack11111_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨ⎯"), bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⎰")) == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⎱"):
                    bstack11llllll_opy_ = {
                        bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⎲"): uuid4().__str__(),
                        bstack11111_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⎳"): bstack1l1lll11_opy_(),
                        bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎴"): bstack1l1lll11_opy_()
                    }
                    _11llll1l_opy_[item.nodeid] = {**_11llll1l_opy_[item.nodeid], **bstack11llllll_opy_}
                    bstack1lll1ll1l11l_opy_(item, _11llll1l_opy_[item.nodeid], bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⎵"))
                    bstack1lll1ll1l11l_opy_(item, _11llll1l_opy_[item.nodeid], bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⎶"), report, call)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡿࢂ࠭⎷"), str(err))
def bstack1lll1ll11111_opy_(test, bstack11llllll_opy_, result=None, call=None, bstack1l11111l1l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1ll1l11l_opy_ = {
        bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⎸"): bstack11llllll_opy_[bstack11111_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⎹")],
        bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩ⎺"): bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࠪ⎻"),
        bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⎼"): test.name,
        bstack11111_opy_ (u"ࠧࡣࡱࡧࡽࠬ⎽"): {
            bstack11111_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭⎾"): bstack11111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ⎿"),
            bstack11111_opy_ (u"ࠪࡧࡴࡪࡥࠨ⏀"): inspect.getsource(test.obj)
        },
        bstack11111_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ⏁"): test.name,
        bstack11111_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫ⏂"): test.name,
        bstack11111_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭⏃"): bstack1l11lll1_opy_.bstack1lllll11_opy_(test),
        bstack11111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ⏄"): file_path,
        bstack11111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪ⏅"): file_path,
        bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⏆"): bstack11111_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⏇"),
        bstack11111_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩ⏈"): file_path,
        bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⏉"): bstack11llllll_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⏊")],
        bstack11111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ⏋"): bstack11111_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ⏌"),
        bstack11111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬ⏍"): {
            bstack11111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧ⏎"): test.nodeid
        },
        bstack11111_opy_ (u"ࠫࡹࡧࡧࡴࠩ⏏"): bstack111l1l1ll1l_opy_(test.own_markers)
    }
    if bstack1l11111l1l_opy_ in [bstack11111_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⏐"), bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⏑")]:
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠧ࡮ࡧࡷࡥࠬ⏒")] = {
            bstack11111_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⏓"): bstack11llllll_opy_.get(bstack11111_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ⏔"), [])
        }
    if bstack1l11111l1l_opy_ == bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫ⏕"):
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏖")] = bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⏗")
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⏘")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⏙")]
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⏚")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏛")]
    if result:
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏜")] = result.outcome
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏝")] = result.duration * 1000
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏞")] = bstack11llllll_opy_[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏟")]
        if result.failed:
            bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⏠")] = bstack11lllll1_opy_.bstack11111111ll_opy_(call.excinfo.typename)
            bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⏡")] = bstack11lllll1_opy_.bstack1llll11ll1ll_opy_(call.excinfo, result)
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⏢")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⏣")]
    if outcome:
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏤")] = bstack1111l11ll1l_opy_(outcome)
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⏥")] = 0
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏦")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⏧")]
        if bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⏨")] == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⏩"):
            bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ⏪")] = bstack11111_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬ⏫")  # bstack1lll1l1lll1l_opy_
            bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⏬")] = [{bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⏭"): [bstack11111_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫ⏮")]}]
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⏯")] = bstack11llllll_opy_[bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⏰")]
    return bstack1ll1l11l_opy_
def bstack1lll1lll1111_opy_(test, bstack1ll111ll_opy_, bstack1l11111l1l_opy_, result, call, outcome, bstack1lll1ll1ll11_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭⏱")]
    hook_name = bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ⏲")]
    hook_data = {
        bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪ⏳"): bstack1ll111ll_opy_[bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⏴")],
        bstack11111_opy_ (u"ࠧࡵࡻࡳࡩࠬ⏵"): bstack11111_opy_ (u"ࠨࡪࡲࡳࡰ࠭⏶"),
        bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⏷"): bstack11111_opy_ (u"ࠪࡿࢂ࠭⏸").format(bstack11l1111l11l_opy_(hook_name)),
        bstack11111_opy_ (u"ࠫࡧࡵࡤࡺࠩ⏹"): {
            bstack11111_opy_ (u"ࠬࡲࡡ࡯ࡩࠪ⏺"): bstack11111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭⏻"),
            bstack11111_opy_ (u"ࠧࡤࡱࡧࡩࠬ⏼"): None
        },
        bstack11111_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧ⏽"): test.name,
        bstack11111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩ⏾"): bstack1l11lll1_opy_.bstack1lllll11_opy_(test, hook_name),
        bstack11111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭⏿"): file_path,
        bstack11111_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭␀"): file_path,
        bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ␁"): bstack11111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ␂"),
        bstack11111_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬ␃"): file_path,
        bstack11111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ␄"): bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭␅")],
        bstack11111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭␆"): bstack11111_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭␇") if bstack1lll1lll1lll_opy_ == bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ␈") else bstack11111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭␉"),
        bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ␊"): hook_type
    }
    bstack1l1111l111l_opy_ = bstack1ll1ll11_opy_(_11llll1l_opy_.get(test.nodeid, None))
    if bstack1l1111l111l_opy_:
        hook_data[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭␋")] = bstack1l1111l111l_opy_
    if result:
        hook_data[bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ␌")] = result.outcome
        hook_data[bstack11111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ␍")] = result.duration * 1000
        hook_data[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ␎")] = bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ␏")]
        if result.failed:
            hook_data[bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ␐")] = bstack11lllll1_opy_.bstack11111111ll_opy_(call.excinfo.typename)
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ␑")] = bstack11lllll1_opy_.bstack1llll11ll1ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ␒")] = bstack1111l11ll1l_opy_(outcome)
        hook_data[bstack11111_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ␓")] = 100
        hook_data[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ␔")] = bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ␕")]
        if hook_data[bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ␖")] == bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭␗"):
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭␘")] = bstack11111_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩ␙")  # bstack1lll1l1lll1l_opy_
            hook_data[bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ␚")] = [{bstack11111_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭␛"): [bstack11111_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨ␜")]}]
    if bstack1lll1ll1ll11_opy_:
        hook_data[bstack11111_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ␝")] = bstack1lll1ll1ll11_opy_.result
        hook_data[bstack11111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ␞")] = bstack111l11ll111_opy_(bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ␟")], bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭␠")])
        hook_data[bstack11111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ␡")] = bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ␢")]
        if hook_data[bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ␣")] == bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ␤"):
            hook_data[bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ␥")] = bstack11lllll1_opy_.bstack11111111ll_opy_(bstack1lll1ll1ll11_opy_.exception_type)
            hook_data[bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ␦")] = [{bstack11111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ␧"): bstack1111l1l1111_opy_(bstack1lll1ll1ll11_opy_.exception)}]
    return hook_data
def bstack1lll1ll1l11l_opy_(test, bstack11llllll_opy_, bstack1l11111l1l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11111_opy_ (u"ࠩࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡨࡺࡪࡴࡴ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠡ࠯ࠣࡿࢂ࠭␨").format(bstack1l11111l1l_opy_))
    bstack1ll1l11l_opy_ = bstack1lll1ll11111_opy_(test, bstack11llllll_opy_, result, call, bstack1l11111l1l_opy_, outcome)
    driver = getattr(test, bstack11111_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ␩"), None)
    if bstack1l11111l1l_opy_ == bstack11111_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ␪") and driver:
        bstack1ll1l11l_opy_[bstack11111_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫ␫")] = bstack11lllll1_opy_.bstack1lll1ll1_opy_(driver)
    if bstack1l11111l1l_opy_ == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ␬"):
        bstack1l11111l1l_opy_ = bstack11111_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ␭")
    bstack1l1l1lll_opy_ = {
        bstack11111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ␮"): bstack1l11111l1l_opy_,
        bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ␯"): bstack1ll1l11l_opy_
    }
    bstack11lllll1_opy_.bstack1l1l1l11_opy_(bstack1l1l1lll_opy_)
    if bstack1l11111l1l_opy_ == bstack11111_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ␰"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ␱"): bstack11111_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭␲")}
    elif bstack1l11111l1l_opy_ == bstack11111_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ␳"):
        threading.current_thread().bstackTestMeta = {bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ␴"): getattr(result, bstack11111_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ␵"), bstack11111_opy_ (u"ࠩࠪ␶"))}
def bstack1lll1l1lllll_opy_(test, bstack11llllll_opy_, bstack1l11111l1l_opy_, result=None, call=None, outcome=None, bstack1lll1ll1ll11_opy_=None):
    logger.debug(bstack11111_opy_ (u"ࠪࡷࡪࡴࡤࡠࡪࡲࡳࡰࡥࡲࡶࡰࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥ࡮࡯ࡰ࡭ࠣࡨࡦࡺࡡ࠭ࠢࡨࡺࡪࡴࡴࡕࡻࡳࡩࠥ࠳ࠠࡼࡿࠪ␷").format(bstack1l11111l1l_opy_))
    hook_data = bstack1lll1lll1111_opy_(test, bstack11llllll_opy_, bstack1l11111l1l_opy_, result, call, outcome, bstack1lll1ll1ll11_opy_)
    bstack1l1l1lll_opy_ = {
        bstack11111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ␸"): bstack1l11111l1l_opy_,
        bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧ␹"): hook_data
    }
    bstack11lllll1_opy_.bstack1l1l1l11_opy_(bstack1l1l1lll_opy_)
def bstack1ll1ll11_opy_(bstack11llllll_opy_):
    if not bstack11llllll_opy_:
        return None
    if bstack11llllll_opy_.get(bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ␺"), None):
        return getattr(bstack11llllll_opy_[bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ␻")], bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭␼"), None)
    return bstack11llllll_opy_.get(bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ␽"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG, bstack1lll1ll1l1l_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_.LOG, bstack1lll1ll1l1l_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack11lllll1_opy_.on():
            return
        places = [bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ␾"), bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ␿"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ⑀")]
        logs = []
        for bstack1lll1lll1l1l_opy_ in places:
            records = caplog.get_records(bstack1lll1lll1l1l_opy_)
            bstack1lll1lll1l11_opy_ = bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⑁") if bstack1lll1lll1l1l_opy_ == bstack11111_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ⑂") else bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⑃")
            bstack1lll1l1lll11_opy_ = request.node.nodeid + (bstack11111_opy_ (u"ࠩࠪ⑄") if bstack1lll1lll1l1l_opy_ == bstack11111_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ⑅") else bstack11111_opy_ (u"ࠫ࠲࠭⑆") + bstack1lll1lll1l1l_opy_)
            test_uuid = bstack1ll1ll11_opy_(_11llll1l_opy_.get(bstack1lll1l1lll11_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack1111l11l11l_opy_(record.message):
                    continue
                logs.append({
                    bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⑇"): bstack111l111llll_opy_(record.created).isoformat() + bstack11111_opy_ (u"࡚࠭ࠨ⑈"),
                    bstack11111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⑉"): record.levelname,
                    bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⑊"): record.message,
                    bstack1lll1lll1l11_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack11lllll1_opy_.bstack1l11l1ll_opy_(logs)
    except Exception as err:
        print(bstack11111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭⑋"), str(err))
def bstack11lll1l111_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l111111l_opy_
    bstack1llllll1ll_opy_ = bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ⑌"), None) and bstack1lll1lll_opy_(
            threading.current_thread(), bstack11111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ⑍"), None)
    bstack11l1l1lll1_opy_ = getattr(driver, bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ⑎"), None) != None and getattr(driver, bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭⑏"), None) == True
    if sequence == bstack11111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ⑐") and driver != None:
      if not bstack1l111111l_opy_ and bstack1lll11ll11l_opy_() and bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⑑") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⑒")] == True and bstack11l1lll1l_opy_.bstack1llllll11l_opy_(driver_command) and (bstack11l1l1lll1_opy_ or bstack1llllll1ll_opy_) and not bstack1l11l1l1ll_opy_(args):
        try:
          bstack1l111111l_opy_ = True
          logger.debug(bstack11111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬ⑓").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩ⑔").format(str(err)))
        bstack1l111111l_opy_ = False
    if sequence == bstack11111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ⑕"):
        if driver_command == bstack11111_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ⑖"):
            bstack11lllll1_opy_.bstack1l11l1l1l_opy_({
                bstack11111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭⑗"): response[bstack11111_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ⑘")],
                bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⑙"): store[bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⑚")]
            })
def bstack11l1l1111l_opy_():
    global bstack11ll11l1ll_opy_
    bstack111111l11l_opy_.bstack1l111l1ll_opy_()
    logging.shutdown()
    bstack11lllll1_opy_.bstack1lll1111_opy_()
    for driver in bstack11ll11l1ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1ll111l1_opy_(*args):
    global bstack11ll11l1ll_opy_
    bstack11lllll1_opy_.bstack1lll1111_opy_()
    for driver in bstack11ll11l1ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack111l1l11l_opy_, bstack111111111_opy_=bstack11ll11111_opy_)
def bstack1l11ll1lll_opy_(self, *args, **kwargs):
    bstack11lllll1l_opy_ = bstack1l1l11ll1l_opy_(self, *args, **kwargs)
    bstack11l111111l_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ⑛"), None)
    if bstack11l111111l_opy_ and bstack11l111111l_opy_.get(bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⑜"), bstack11111_opy_ (u"࠭ࠧ⑝")) == bstack11111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ⑞"):
        bstack11lllll1_opy_.bstack111ll1ll11_opy_(self)
    return bstack11lllll1l_opy_
@measure(event_name=EVENTS.bstack1l1l111l1l_opy_, stage=STAGE.bstack1ll1111ll_opy_, bstack111111111_opy_=bstack11ll11111_opy_)
def bstack1l111ll1ll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack111lll11_opy_ = Config.bstack1111llll_opy_()
    if bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ⑟")):
        return
    bstack111lll11_opy_.set_property(bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭①"), True)
    global bstack1111ll111l_opy_
    global bstack1ll1l11l1_opy_
    bstack1111ll111l_opy_ = framework_name
    logger.info(bstack111l1l11ll_opy_.format(bstack1111ll111l_opy_.split(bstack11111_opy_ (u"ࠪ࠱ࠬ②"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll11ll11l_opy_():
            Service.start = bstack1l1ll11ll1_opy_
            Service.stop = bstack11ll1l1ll1_opy_
            webdriver.Remote.get = bstack111l1ll1l1_opy_
            webdriver.Remote.__init__ = bstack111ll111l_opy_
            if not isinstance(os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬ③")), str):
                return
            WebDriver.quit = bstack1l1l111l1_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack11lllll1_opy_.on():
            webdriver.Remote.__init__ = bstack1l11ll1lll_opy_
        bstack1ll1l11l1_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11111_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪ④")):
        bstack1ll1l11l1_opy_ = eval(os.environ.get(bstack11111_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫ⑤")))
    if not bstack1ll1l11l1_opy_:
        bstack1l11l1l111_opy_(bstack11111_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤ⑥"), bstack1l111l1l1_opy_)
    if bstack111llll1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11111_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⑦")) and callable(getattr(RemoteConnection, bstack11111_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ⑧"))):
                RemoteConnection._get_proxy_url = bstack1l1l1l1ll1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack1l1l1l1ll1_opy_
        except Exception as e:
            logger.error(bstack1l111l11ll_opy_.format(str(e)))
    if bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⑨") in str(framework_name).lower():
        if not bstack1lll11ll11l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1llll1lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l1l1l_opy_
            Config.getoption = bstack11llll11l1_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l1ll1llll_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll111l11_opy_, stage=STAGE.bstack111l1l11l_opy_, bstack111111111_opy_=bstack11ll11111_opy_)
def bstack1l1l111l1_opy_(self):
    global bstack1111ll111l_opy_
    global bstack1ll1l1ll1l_opy_
    global bstack1l111ll111_opy_
    try:
        if bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⑩") in bstack1111ll111l_opy_ and self.session_id != None and bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩ⑪"), bstack11111_opy_ (u"࠭ࠧ⑫")) != bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⑬"):
            bstack111llll1ll_opy_ = bstack11111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⑭") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⑮")
            bstack11ll1l1ll_opy_(logger, True)
            if os.environ.get(bstack11111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⑯"), None):
                self.execute_script(
                    bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ⑰") + json.dumps(
                        os.environ.get(bstack11111_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ⑱"))) + bstack11111_opy_ (u"࠭ࡽࡾࠩ⑲"))
            if self != None:
                bstack11l1ll1111_opy_(self, bstack111llll1ll_opy_, bstack11111_opy_ (u"ࠧ࠭ࠢࠪ⑳").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l1l1l1l1_opy_(bstack1l1l11l11l1_opy_):
            item = store.get(bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⑴"), None)
            if item is not None and bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⑵"), None):
                bstack1llllll1l_opy_.bstack1lll11ll1_opy_(self, bstack1ll1l11l11_opy_, logger, item)
        threading.current_thread().testStatus = bstack11111_opy_ (u"ࠪࠫ⑶")
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧ⑷") + str(e))
    bstack1l111ll111_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1lllll11l1_opy_, stage=STAGE.bstack111l1l11l_opy_, bstack111111111_opy_=bstack11ll11111_opy_)
def bstack111ll111l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll1l1ll1l_opy_
    global bstack11ll11111_opy_
    global bstack1l11lll111_opy_
    global bstack1111ll111l_opy_
    global bstack1l1l11ll1l_opy_
    global bstack11ll11l1ll_opy_
    global bstack111l11111l_opy_
    global bstack1ll111l11l_opy_
    global bstack1ll1l11l11_opy_
    CONFIG[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ⑸")] = str(bstack1111ll111l_opy_) + str(__version__)
    command_executor = bstack1111l1ll11_opy_(bstack111l11111l_opy_, CONFIG)
    logger.debug(bstack1lllllll1l_opy_.format(command_executor))
    proxy = bstack1l1l1l1111_opy_(CONFIG, proxy)
    bstack11ll11lll_opy_ = 0
    try:
        if bstack1l11lll111_opy_ is True:
            bstack11ll11lll_opy_ = int(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⑹")))
    except:
        bstack11ll11lll_opy_ = 0
    bstack1111ll11l_opy_ = bstack1l1111llll_opy_(CONFIG, bstack11ll11lll_opy_)
    logger.debug(bstack11lll111l_opy_.format(str(bstack1111ll11l_opy_)))
    bstack1ll1l11l11_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⑺"))[bstack11ll11lll_opy_]
    if bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ⑻") in CONFIG and CONFIG[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭⑼")]:
        bstack111l1l11l1_opy_(bstack1111ll11l_opy_, bstack1ll111l11l_opy_)
    if bstack111111l1_opy_.bstack1111ll1l1l_opy_(CONFIG, bstack11ll11lll_opy_) and bstack111111l1_opy_.bstack1111lllll1_opy_(bstack1111ll11l_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l1l1l1l1_opy_(bstack1l1l11l11l1_opy_):
            bstack111111l1_opy_.set_capabilities(bstack1111ll11l_opy_, CONFIG)
    if desired_capabilities:
        bstack1l1lllll11_opy_ = bstack1111ll11l1_opy_(desired_capabilities)
        bstack1l1lllll11_opy_[bstack11111_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ⑽")] = bstack1l1lll1lll_opy_(CONFIG)
        bstack1l1llll11_opy_ = bstack1l1111llll_opy_(bstack1l1lllll11_opy_)
        if bstack1l1llll11_opy_:
            bstack1111ll11l_opy_ = update(bstack1l1llll11_opy_, bstack1111ll11l_opy_)
        desired_capabilities = None
    if options:
        bstack1l111l1ll1_opy_(options, bstack1111ll11l_opy_)
    if not options:
        options = bstack1lllll11ll_opy_(bstack1111ll11l_opy_)
    if proxy and bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ⑾")):
        options.proxy(proxy)
    if options and bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ⑿")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1llllll_opy_() < version.parse(bstack11111_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ⒀")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1111ll11l_opy_)
    logger.info(bstack1111l1lll_opy_)
    bstack1ll11111ll_opy_.end(EVENTS.bstack1l1l111l1l_opy_.value, EVENTS.bstack1l1l111l1l_opy_.value + bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ⒁"),
                               EVENTS.bstack1l1l111l1l_opy_.value + bstack11111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ⒂"), True, None)
    try:
        if bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ⒃")):
            bstack1l1l11ll1l_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ⒄")):
            bstack1l1l11ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ⒅")):
            bstack1l1l11ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack1l1l11ll1l_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack1ll1l11111_opy_:
        logger.error(bstack1l1ll1l11l_opy_.format(bstack11111_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠫ⒆"), str(bstack1ll1l11111_opy_)))
        raise bstack1ll1l11111_opy_
    try:
        bstack11lll1llll_opy_ = bstack11111_opy_ (u"࠭ࠧ⒇")
        if bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨ⒈")):
            bstack11lll1llll_opy_ = self.caps.get(bstack11111_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ⒉"))
        else:
            bstack11lll1llll_opy_ = self.capabilities.get(bstack11111_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ⒊"))
        if bstack11lll1llll_opy_:
            bstack111lll11ll_opy_(bstack11lll1llll_opy_)
            if bstack1l1llllll_opy_() <= version.parse(bstack11111_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ⒋")):
                self.command_executor._url = bstack11111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ⒌") + bstack111l11111l_opy_ + bstack11111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ⒍")
            else:
                self.command_executor._url = bstack11111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ⒎") + bstack11lll1llll_opy_ + bstack11111_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ⒏")
            logger.debug(bstack1l11l11111_opy_.format(bstack11lll1llll_opy_))
        else:
            logger.debug(bstack1l1l11l111_opy_.format(bstack11111_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤ⒐")))
    except Exception as e:
        logger.debug(bstack1l1l11l111_opy_.format(e))
    bstack1ll1l1ll1l_opy_ = self.session_id
    if bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ⒑") in bstack1111ll111l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⒒"), None)
        if item:
            bstack1lll1ll11l1l_opy_ = getattr(item, bstack11111_opy_ (u"ࠫࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࡠࡵࡷࡥࡷࡺࡥࡥࠩ⒓"), False)
            if not getattr(item, bstack11111_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⒔"), None) and bstack1lll1ll11l1l_opy_:
                setattr(store[bstack11111_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⒕")], bstack11111_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⒖"), self)
        bstack11l111111l_opy_ = getattr(threading.current_thread(), bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩ⒗"), None)
        if bstack11l111111l_opy_ and bstack11l111111l_opy_.get(bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⒘"), bstack11111_opy_ (u"ࠪࠫ⒙")) == bstack11111_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⒚"):
            bstack11lllll1_opy_.bstack111ll1ll11_opy_(self)
    bstack11ll11l1ll_opy_.append(self)
    if bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⒛") in CONFIG and bstack11111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⒜") in CONFIG[bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⒝")][bstack11ll11lll_opy_]:
        bstack11ll11111_opy_ = CONFIG[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⒞")][bstack11ll11lll_opy_][bstack11111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⒟")]
    logger.debug(bstack1l1ll1lll_opy_.format(bstack1ll1l1ll1l_opy_))
@measure(event_name=EVENTS.bstack1l1l1l111l_opy_, stage=STAGE.bstack111l1l11l_opy_, bstack111111111_opy_=bstack11ll11111_opy_)
def bstack111l1ll1l1_opy_(self, url):
    global bstack111l1l111l_opy_
    global CONFIG
    try:
        bstack11ll11lll1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11ll11l1l1_opy_.format(str(err)))
    try:
        bstack111l1l111l_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1l11ll111l_opy_):
                bstack11ll11lll1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11ll11l1l1_opy_.format(str(err)))
        raise e
def bstack1lll11l1l1_opy_(item, when):
    global bstack11111ll1l_opy_
    try:
        bstack11111ll1l_opy_(item, when)
    except Exception as e:
        pass
def bstack1l1ll1llll_opy_(item, call, rep):
    global bstack1l1l11l1ll_opy_
    global bstack11ll11l1ll_opy_
    name = bstack11111_opy_ (u"ࠪࠫ⒠")
    try:
        if rep.when == bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ⒡"):
            bstack1ll1l1ll1l_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⒢"))
            try:
                if (str(skipSessionName).lower() != bstack11111_opy_ (u"࠭ࡴࡳࡷࡨࠫ⒣")):
                    name = str(rep.nodeid)
                    bstack11ll1ll11l_opy_ = bstack1l1111111l_opy_(bstack11111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⒤"), name, bstack11111_opy_ (u"ࠨࠩ⒥"), bstack11111_opy_ (u"ࠩࠪ⒦"), bstack11111_opy_ (u"ࠪࠫ⒧"), bstack11111_opy_ (u"ࠫࠬ⒨"))
                    os.environ[bstack11111_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ⒩")] = name
                    for driver in bstack11ll11l1ll_opy_:
                        if bstack1ll1l1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack11ll1ll11l_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭⒪").format(str(e)))
            try:
                bstack1lll1lllll_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⒫"):
                    status = bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⒬") if rep.outcome.lower() == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⒭") else bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⒮")
                    reason = bstack11111_opy_ (u"ࠫࠬ⒯")
                    if status == bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ⒰"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11111_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ⒱") if status == bstack11111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⒲") else bstack11111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ⒳")
                    data = name + bstack11111_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ⒴") if status == bstack11111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⒵") else name + bstack11111_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧⒶ") + reason
                    bstack1l1ll111l_opy_ = bstack1l1111111l_opy_(bstack11111_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧⒷ"), bstack11111_opy_ (u"࠭ࠧⒸ"), bstack11111_opy_ (u"ࠧࠨⒹ"), bstack11111_opy_ (u"ࠨࠩⒺ"), level, data)
                    for driver in bstack11ll11l1ll_opy_:
                        if bstack1ll1l1ll1l_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll111l_opy_)
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭Ⓕ").format(str(e)))
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧⒼ").format(str(e)))
    bstack1l1l11l1ll_opy_(item, call, rep)
notset = Notset()
def bstack11llll11l1_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11l11ll1l1_opy_
    if str(name).lower() == bstack11111_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫⒽ"):
        return bstack11111_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦⒾ")
    else:
        return bstack11l11ll1l1_opy_(self, name, default, skip)
def bstack1l1l1l1ll1_opy_(self):
    global CONFIG
    global bstack11ll1ll1l1_opy_
    try:
        proxy = bstack1lll11l11l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11111_opy_ (u"࠭࠮ࡱࡣࡦࠫⒿ")):
                proxies = bstack1ll1ll11l1_opy_(proxy, bstack1111l1ll11_opy_())
                if len(proxies) > 0:
                    protocol, bstack111l1lllll_opy_ = proxies.popitem()
                    if bstack11111_opy_ (u"ࠢ࠻࠱࠲ࠦⓀ") in bstack111l1lllll_opy_:
                        return bstack111l1lllll_opy_
                    else:
                        return bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤⓁ") + bstack111l1lllll_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨⓂ").format(str(e)))
    return bstack11ll1ll1l1_opy_(self)
def bstack111llll1l_opy_():
    return (bstack11111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭Ⓝ") in CONFIG or bstack11111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨⓄ") in CONFIG) and bstack11l111lll1_opy_() and bstack1l1llllll_opy_() >= version.parse(
        bstack1111l11l11_opy_)
def bstack11lll11lll_opy_(self,
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
    global bstack11ll11111_opy_
    global bstack1l11lll111_opy_
    global bstack1111ll111l_opy_
    CONFIG[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧⓅ")] = str(bstack1111ll111l_opy_) + str(__version__)
    bstack11ll11lll_opy_ = 0
    try:
        if bstack1l11lll111_opy_ is True:
            bstack11ll11lll_opy_ = int(os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭Ⓠ")))
    except:
        bstack11ll11lll_opy_ = 0
    CONFIG[bstack11111_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨⓇ")] = True
    bstack1111ll11l_opy_ = bstack1l1111llll_opy_(CONFIG, bstack11ll11lll_opy_)
    logger.debug(bstack11lll111l_opy_.format(str(bstack1111ll11l_opy_)))
    if CONFIG.get(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬⓈ")):
        bstack111l1l11l1_opy_(bstack1111ll11l_opy_, bstack1ll111l11l_opy_)
    if bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬⓉ") in CONFIG and bstack11111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨⓊ") in CONFIG[bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧⓋ")][bstack11ll11lll_opy_]:
        bstack11ll11111_opy_ = CONFIG[bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨⓌ")][bstack11ll11lll_opy_][bstack11111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫⓍ")]
    import urllib
    import json
    if bstack11111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫⓎ") in CONFIG and str(CONFIG[bstack11111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬⓏ")]).lower() != bstack11111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨⓐ"):
        bstack11llll1ll1_opy_ = bstack1l1l1111ll_opy_()
        bstack1l11ll1l1l_opy_ = bstack11llll1ll1_opy_ + urllib.parse.quote(json.dumps(bstack1111ll11l_opy_))
    else:
        bstack1l11ll1l1l_opy_ = bstack11111_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬⓑ") + urllib.parse.quote(json.dumps(bstack1111ll11l_opy_))
    browser = self.connect(bstack1l11ll1l1l_opy_)
    return browser
def bstack111l11l111_opy_():
    global bstack1ll1l11l1_opy_
    global bstack1111ll111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11ll1l11l_opy_
        if not bstack1lll11ll11l_opy_():
            global bstack1l111lll1l_opy_
            if not bstack1l111lll1l_opy_:
                from bstack_utils.helper import bstack1l11l1l11l_opy_, bstack11llll111_opy_
                bstack1l111lll1l_opy_ = bstack1l11l1l11l_opy_()
                bstack11llll111_opy_(bstack1111ll111l_opy_)
            BrowserType.connect = bstack11ll1l11l_opy_
            return
        BrowserType.launch = bstack11lll11lll_opy_
        bstack1ll1l11l1_opy_ = True
    except Exception as e:
        pass
def bstack1lll1lll11l1_opy_():
    global CONFIG
    global bstack11l11l1111_opy_
    global bstack111l11111l_opy_
    global bstack1ll111l11l_opy_
    global bstack1l11lll111_opy_
    global bstack1l1lll1l1_opy_
    CONFIG = json.loads(os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪⓒ")))
    bstack11l11l1111_opy_ = eval(os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ⓓ")))
    bstack111l11111l_opy_ = os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭ⓔ"))
    bstack11l1111l1l_opy_(CONFIG, bstack11l11l1111_opy_)
    bstack1l1lll1l1_opy_ = bstack111111l11l_opy_.configure_logger(CONFIG, bstack1l1lll1l1_opy_)
    if cli.bstack11l11ll11l_opy_():
        bstack111llllll_opy_.invoke(Events.CONNECT, bstack11l1l11l1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧⓕ"), bstack11111_opy_ (u"ࠨ࠲ࠪⓖ")))
        cli.bstack1l11ll11l1l_opy_(cli_context.platform_index)
        cli.bstack1l1l1l1l111_opy_(bstack1111l1ll11_opy_(bstack111l11111l_opy_, CONFIG), cli_context.platform_index, bstack1lllll11ll_opy_)
        cli.bstack1l1l1l111ll_opy_()
        logger.debug(bstack11111_opy_ (u"ࠤࡆࡐࡎࠦࡩࡴࠢࡤࡧࡹ࡯ࡶࡦࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣⓗ") + str(cli_context.platform_index) + bstack11111_opy_ (u"ࠥࠦⓘ"))
        return # skip all existing operations
    global bstack1l1l11ll1l_opy_
    global bstack1l111ll111_opy_
    global bstack11ll11l11_opy_
    global bstack11l1l1l111_opy_
    global bstack1l11l1111_opy_
    global bstack1lllllllll_opy_
    global bstack11l11l1ll_opy_
    global bstack111l1l111l_opy_
    global bstack11ll1ll1l1_opy_
    global bstack11l11ll1l1_opy_
    global bstack11111ll1l_opy_
    global bstack1l1l11l1ll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l1l11ll1l_opy_ = webdriver.Remote.__init__
        bstack1l111ll111_opy_ = WebDriver.quit
        bstack11l11l1ll_opy_ = WebDriver.close
        bstack111l1l111l_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧⓙ") in CONFIG or bstack11111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩⓚ") in CONFIG) and bstack11l111lll1_opy_():
        if bstack1l1llllll_opy_() < version.parse(bstack1111l11l11_opy_):
            logger.error(bstack1ll11l1l11_opy_.format(bstack1l1llllll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11111_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧⓛ")) and callable(getattr(RemoteConnection, bstack11111_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨⓜ"))):
                    bstack11ll1ll1l1_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack11ll1ll1l1_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack1l111l11ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11l11ll1l1_opy_ = Config.getoption
        from _pytest import runner
        bstack11111ll1l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11111lll_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l1l11l1ll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩⓝ"))
    bstack1ll111l11l_opy_ = CONFIG.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ⓞ"), {}).get(bstack11111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬⓟ"))
    bstack1l11lll111_opy_ = True
    bstack1l111ll1ll_opy_(bstack111llllll1_opy_)
if (bstack111l1111ll1_opy_()):
    bstack1lll1lll11l1_opy_()
@error_handler(class_method=False)
def bstack1lll1ll11lll_opy_(hook_name, event, bstack1ll1l1l1111_opy_=None):
    if hook_name not in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬⓠ"), bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩⓡ"), bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬⓢ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩⓣ"), bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ⓤ"), bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪⓥ"), bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩⓦ"), bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ⓧ")]:
        return
    node = store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩⓨ")]
    if hook_name in [bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬⓩ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ⓪")]:
        node = store[bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ⓫")]
    elif hook_name in [bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ⓬"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ⓭")]:
        node = store[bstack11111_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ⓮")]
    hook_type = bstack11l1111l1ll_opy_(hook_name)
    if event == bstack11111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ⓯"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_[hook_type], bstack1lll1ll1l1l_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1ll111ll_opy_ = {
            bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⓰"): uuid,
            bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⓱"): bstack1l1lll11_opy_(),
            bstack11111_opy_ (u"ࠨࡶࡼࡴࡪ࠭⓲"): bstack11111_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⓳"),
            bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭⓴"): hook_type,
            bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ⓵"): hook_name
        }
        store[bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⓶")].append(uuid)
        bstack1lll1ll1l1l1_opy_ = node.nodeid
        if hook_type == bstack11111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ⓷"):
            if not _11llll1l_opy_.get(bstack1lll1ll1l1l1_opy_, None):
                _11llll1l_opy_[bstack1lll1ll1l1l1_opy_] = {bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⓸"): []}
            _11llll1l_opy_[bstack1lll1ll1l1l1_opy_][bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⓹")].append(bstack1ll111ll_opy_[bstack11111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⓺")])
        _11llll1l_opy_[bstack1lll1ll1l1l1_opy_ + bstack11111_opy_ (u"ࠪ࠱ࠬ⓻") + hook_name] = bstack1ll111ll_opy_
        bstack1lll1l1lllll_opy_(node, bstack1ll111ll_opy_, bstack11111_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⓼"))
    elif event == bstack11111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ⓽"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1ll111l_opy_[hook_type], bstack1lll1ll1l1l_opy_.POST, node, None, bstack1ll1l1l1111_opy_)
            return
        bstack1ll11ll1_opy_ = node.nodeid + bstack11111_opy_ (u"࠭࠭ࠨ⓾") + hook_name
        _11llll1l_opy_[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⓿")] = bstack1l1lll11_opy_()
        bstack1lll1ll11l11_opy_(_11llll1l_opy_[bstack1ll11ll1_opy_][bstack11111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭─")])
        bstack1lll1l1lllll_opy_(node, _11llll1l_opy_[bstack1ll11ll1_opy_], bstack11111_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ━"), bstack1lll1ll1ll11_opy_=bstack1ll1l1l1111_opy_)
def bstack1lll1llll111_opy_():
    global bstack1lll1lll1lll_opy_
    if bstack11l111ll1l_opy_():
        bstack1lll1lll1lll_opy_ = bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧ│")
    else:
        bstack1lll1lll1lll_opy_ = bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ┃")
@bstack11lllll1_opy_.bstack1llll11l11ll_opy_
def bstack1lll1l1llll1_opy_():
    bstack1lll1llll111_opy_()
    if cli.is_running():
        try:
            bstack11l1l1ll11l_opy_(bstack1lll1ll11lll_opy_)
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨ┄").format(e))
        return
    if bstack11l111lll1_opy_():
        bstack111lll11_opy_ = Config.bstack1111llll_opy_()
        bstack11111_opy_ (u"࠭ࠧࠨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡵࡶࡰࠡ࠿ࠣ࠵࠱ࠦ࡭ࡰࡦࡢࡩࡽ࡫ࡣࡶࡶࡨࠤ࡬࡫ࡴࡴࠢࡸࡷࡪࡪࠠࡧࡱࡵࠤࡦ࠷࠱ࡺࠢࡦࡳࡲࡳࡡ࡯ࡦࡶ࠱ࡼࡸࡡࡱࡲ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡲࡳࡴࠥࡄࠠ࠲࠮ࠣࡱࡴࡪ࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡣࡧࡦࡥࡺࡹࡥࠡ࡫ࡷࠤ࡮ࡹࠠࡱࡣࡷࡧ࡭࡫ࡤࠡ࡫ࡱࠤࡦࠦࡤࡪࡨࡩࡩࡷ࡫࡮ࡵࠢࡳࡶࡴࡩࡥࡴࡵࠣ࡭ࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡵࡴࠢࡺࡩࠥࡴࡥࡦࡦࠣࡸࡴࠦࡵࡴࡧࠣࡗࡪࡲࡥ࡯࡫ࡸࡱࡕࡧࡴࡤࡪࠫࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡮ࡡ࡯ࡦ࡯ࡩࡷ࠯ࠠࡧࡱࡵࠤࡵࡶࡰࠡࡀࠣ࠵ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧࠨࠩ┅")
        if bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ┆")):
            if CONFIG.get(bstack11111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ┇")) is not None and int(CONFIG[bstack11111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ┈")]) > 1:
                bstack1lll11l111_opy_(bstack11lll1l111_opy_)
            return
        bstack1lll11l111_opy_(bstack11lll1l111_opy_)
    try:
        bstack11l1l1ll11l_opy_(bstack1lll1ll11lll_opy_)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࡳࠡࡲࡤࡸࡨ࡮࠺ࠡࡽࢀࠦ┉").format(e))
bstack1lll1l1llll1_opy_()