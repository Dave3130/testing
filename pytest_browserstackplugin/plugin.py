# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack11l1l1ll11_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l1lllll11_opy_, bstack1111lll1l1_opy_, update, bstack1111111l1_opy_,
                                       bstack1l1llll11l_opy_, bstack1l1ll11ll_opy_, bstack1l111ll1l_opy_, bstack1l1111llll_opy_,
                                       bstack1l11l1l1l1_opy_, bstack1lll11llll_opy_, bstack11l111lll_opy_,
                                       bstack11l1lll1l_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1llllll111_opy_)
from browserstack_sdk.bstack111l111l_opy_ import bstack1lll11lll_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack11l1l1l1ll_opy_
from bstack_utils.capture import bstack1ll1ll1l_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack111l1ll111_opy_, bstack11l1l1l111_opy_, bstack1l1l1ll1l_opy_, \
    bstack11l1ll1111_opy_
from bstack_utils.helper import bstack1l1l11l1_opy_, bstack111l111l1l1_opy_, bstack1l11llll_opy_, bstack11llll1l1l_opy_, bstack1lll1l1ll1l_opy_, bstack1lll1111_opy_, \
    bstack1111l1ll111_opy_, \
    bstack111l11lllll_opy_, bstack11l11l11l1_opy_, bstack1lll11lll1_opy_, bstack1111ll1l1ll_opy_, bstack11l1llll1l_opy_, Notset, \
    bstack1l11l1l1l_opy_, bstack111l111lll1_opy_, bstack111l11lll1l_opy_, Result, bstack1111llll11l_opy_, bstack1111l1lllll_opy_, error_handler, \
    bstack11111l1l1l_opy_, bstack11111l111l_opy_, bstack1lll1l1lll_opy_, bstack111l1111111_opy_
from bstack_utils.bstack11l1ll1111l_opy_ import bstack11l1l1l1l1l_opy_
from bstack_utils.messages import bstack1l11ll111l_opy_, bstack1l1l1l1l1l_opy_, bstack1ll1lll1ll_opy_, bstack1lll1lllll_opy_, bstack1lll1l1ll_opy_, \
    bstack11l1ll1ll1_opy_, bstack1111llllll_opy_, bstack11llll111_opy_, bstack1ll11ll111_opy_, bstack1l1l1l1lll_opy_, \
    bstack11l1111l1l_opy_, bstack11l1111111_opy_, bstack11111l11ll_opy_
from bstack_utils.proxy import bstack111lll1l1l_opy_, bstack111ll1l1ll_opy_
from bstack_utils.bstack11l1l11l1l_opy_ import bstack11l111l1l11_opy_, bstack11l111l1ll1_opy_, bstack11l111l1lll_opy_, bstack11l111l1l1l_opy_, \
    bstack11l111ll1ll_opy_, bstack11l111ll11l_opy_, bstack11l111l111l_opy_, bstack11ll1l11l_opy_, bstack11l111ll111_opy_
from bstack_utils.bstack1lll1l111l_opy_ import bstack11l111ll11_opy_
from bstack_utils.bstack1l1lll11l1_opy_ import bstack11l1l1l11_opy_, bstack1111l1lll_opy_, bstack1lll1ll1ll_opy_, \
    bstack1ll1111111_opy_, bstack111l1l1lll_opy_
from bstack_utils.bstack1l11ll1l_opy_ import bstack1l1l1l11_opy_
from bstack_utils.bstack1l1ll1l1_opy_ import bstack1l1l111l_opy_
import bstack_utils.accessibility as bstack1111ll11_opy_
from bstack_utils.bstack11lll1l1_opy_ import bstack1l111l1l_opy_
from bstack_utils.bstack1l1l1l1l1_opy_ import bstack1l1l1l1l1_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from browserstack_sdk.__init__ import bstack1l1l1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1llll11_opy_ import bstack1l1l11l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1111l11l11_opy_ import bstack1111l11l11_opy_, Events, bstack1l1l11llll_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll11ll1111_opy_, bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1111l11l11_opy_ import bstack1111l11l11_opy_, Events, bstack1l1l11llll_opy_
bstack11ll111l1_opy_ = None
bstack1l111lllll_opy_ = None
bstack11l11l1l1_opy_ = None
bstack111l111lll_opy_ = None
bstack111lll11l1_opy_ = None
bstack1ll111111_opy_ = None
bstack1l11ll1l11_opy_ = None
bstack1l11ll11l_opy_ = None
bstack11ll1l1111_opy_ = None
bstack1l111l1ll1_opy_ = None
bstack111l11l1l1_opy_ = None
bstack11ll111lll_opy_ = None
bstack1ll1l1l11l_opy_ = None
bstack11l11l111l_opy_ = bstack11ll_opy_ (u"ࠬ࠭≹")
CONFIG = {}
bstack1l111ll1l1_opy_ = False
bstack1lllll1l11_opy_ = bstack11ll_opy_ (u"࠭ࠧ≺")
bstack111l1l11l_opy_ = bstack11ll_opy_ (u"ࠧࠨ≻")
bstack11l111ll1l_opy_ = False
bstack1111lll1l_opy_ = []
bstack1ll11l1lll_opy_ = bstack111l1ll111_opy_
bstack1lll1llllll1_opy_ = bstack11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ≼")
bstack1llll11ll1_opy_ = {}
bstack1111llll1_opy_ = None
bstack1ll11l11l_opy_ = False
logger = bstack11l1l1l1ll_opy_.get_logger(__name__, bstack1ll11l1lll_opy_)
store = {
    bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭≽"): []
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
_1l1111ll_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll11ll1111_opy_(
    test_framework_name=bstack1l111l1111_opy_[bstack11ll_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖ࠰ࡆࡉࡊࠧ≾")] if bstack11l1llll1l_opy_() else bstack1l111l1111_opy_[bstack11ll_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࠫ≿")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1ll11lll11_opy_(page, bstack1l111ll111_opy_):
    try:
        page.evaluate(bstack11ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ⊀"),
                      bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ⊁") + json.dumps(
                          bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠢࡾࡿࠥ⊂"))
    except Exception as e:
        print(bstack11ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ⊃"), e)
def bstack11l11l1l1l_opy_(page, message, level):
    try:
        page.evaluate(bstack11ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ⊄"), bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ⊅") + json.dumps(
            message) + bstack11ll_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ⊆") + json.dumps(level) + bstack11ll_opy_ (u"ࠬࢃࡽࠨ⊇"))
    except Exception as e:
        print(bstack11ll_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ⊈"), e)
def pytest_configure(config):
    global bstack1lllll1l11_opy_
    global CONFIG
    bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
    config.args = bstack1l1l111l_opy_.bstack11l11l1111l_opy_(config.args)
    bstack1111l111_opy_.bstack1lllll1lll_opy_(bstack1lll1l1lll_opy_(config.getoption(bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ⊉"))))
    try:
        bstack11l1l1l1ll_opy_.bstack11111l11l11_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack1111l11l11_opy_.invoke(Events.CONNECT, bstack1l1l11llll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⊊"), bstack11ll_opy_ (u"ࠩ࠳ࠫ⊋")))
        config = json.loads(os.environ.get(bstack11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠤ⊌"), bstack11ll_opy_ (u"ࠦࢀࢃࠢ⊍")))
        cli.bstack1l1l11l1l1l_opy_(bstack1lll11lll1_opy_(bstack1lllll1l11_opy_, CONFIG), cli_context.platform_index, bstack1111111l1_opy_)
    if cli.bstack1l1l111l1l1_opy_(bstack1l1l11l1ll1_opy_):
        cli.bstack1l1l1l1l11l_opy_()
        logger.debug(bstack11ll_opy_ (u"ࠧࡉࡌࡊࠢ࡬ࡷࠥࡧࡣࡵ࡫ࡹࡩࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦ⊎") + str(cli_context.platform_index) + bstack11ll_opy_ (u"ࠨࠢ⊏"))
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_ALL, bstack1lll1ll111l_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11ll_opy_ (u"ࠢࡸࡪࡨࡲࠧ⊐"), None)
    if cli.is_running() and when == bstack11ll_opy_ (u"ࠣࡥࡤࡰࡱࠨ⊑"):
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG_REPORT, bstack1lll1ll111l_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11ll_opy_ (u"ࠤࡦࡥࡱࡲࠢ⊒"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ⊓")))
        if not passed:
            config = json.loads(os.environ.get(bstack11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠥ⊔"), bstack11ll_opy_ (u"ࠧࢁࡽࠣ⊕")))
            if bstack111ll1ll_opy_.bstack111l1l1l_opy_(config):
                bstack1llllll111l1_opy_ = bstack111ll1ll_opy_.bstack1111l1ll_opy_(config)
                if item.execution_count > bstack1llllll111l1_opy_:
                    print(bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡶࡪࡺࡲࡪࡧࡶ࠾ࠥ࠭⊖"), report.nodeid, os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⊗")))
                    bstack111ll1ll_opy_.bstack11l1111ll11_opy_(report.nodeid)
            else:
                print(bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠨ⊘"), report.nodeid, os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⊙")))
                bstack111ll1ll_opy_.bstack11l1111ll11_opy_(report.nodeid)
        else:
            print(bstack11ll_opy_ (u"ࠪࡘࡪࡹࡴࠡࡲࡤࡷࡸ࡫ࡤ࠻ࠢࠪ⊚"), report.nodeid, os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⊛")))
    if cli.is_running():
        if when == bstack11ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ⊜"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.POST, item, call, outcome)
        elif when == bstack11ll_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ⊝"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG_REPORT, bstack1lll1ll111l_opy_.POST, item, call, outcome)
        elif when == bstack11ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ⊞"):
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.AFTER_EACH, bstack1lll1ll111l_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⊟"))
    plugins = item.config.getoption(bstack11ll_opy_ (u"ࠤࡳࡰࡺ࡭ࡩ࡯ࡵࠥ⊠"))
    report = outcome.get_result()
    os.environ[bstack11ll_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⊡")] = report.nodeid
    bstack1lll1ll1lll1_opy_(item, call, report)
    if bstack11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤ⊢") not in plugins or bstack11l1llll1l_opy_():
        return
    summary = []
    driver = getattr(item, bstack11ll_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨ⊣"), None)
    page = getattr(item, bstack11ll_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧ⊤"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1lll1llll1ll_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1ll11lll_opy_(item, report, summary, skipSessionName)
def bstack1lll1llll1ll_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⊥") and report.skipped:
        bstack11l111ll111_opy_(report)
    if report.when in [bstack11ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ⊦"), bstack11ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦ⊧")]:
        return
    if not bstack1lll1l1ll1l_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11ll_opy_ (u"ࠪࡸࡷࡻࡥࠨ⊨")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ⊩") + json.dumps(
                    report.nodeid) + bstack11ll_opy_ (u"ࠬࢃࡽࠨ⊪"))
        os.environ[bstack11ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ⊫")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢ⊬").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⊭")))
    bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"ࠤࠥ⊮")
    bstack11l111ll111_opy_(report)
    if not passed:
        try:
            bstack1l11l1111l_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ⊯").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11l1111l_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ⊰")))
        bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"ࠧࠨ⊱")
        if not passed:
            try:
                bstack1l11l1111l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ⊲").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l11l1111l_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ⊳")
                    + json.dumps(bstack11ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤ⊴"))
                    + bstack11ll_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧ⊵")
                )
            else:
                item._driver.execute_script(
                    bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨ⊶")
                    + json.dumps(str(bstack1l11l1111l_opy_))
                    + bstack11ll_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢ⊷")
                )
        except Exception as e:
            summary.append(bstack11ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥ⊸").format(e))
def bstack1lll1ll111l1_opy_(test_name, error_message):
    try:
        bstack1lll1lll1l1l_opy_ = []
        bstack1lll111ll1_opy_ = os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⊹"), bstack11ll_opy_ (u"ࠧ࠱ࠩ⊺"))
        bstack1111l11ll_opy_ = {bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭⊻"): test_name, bstack11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ⊼"): error_message, bstack11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ⊽"): bstack1lll111ll1_opy_}
        bstack1lll1ll1ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ⊾"))
        if os.path.exists(bstack1lll1ll1ll11_opy_):
            with open(bstack1lll1ll1ll11_opy_) as f:
                bstack1lll1lll1l1l_opy_ = json.load(f)
        bstack1lll1lll1l1l_opy_.append(bstack1111l11ll_opy_)
        with open(bstack1lll1ll1ll11_opy_, bstack11ll_opy_ (u"ࠬࡽࠧ⊿")) as f:
            json.dump(bstack1lll1lll1l1l_opy_, f)
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫ⋀") + str(e))
def bstack1lll1ll11lll_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨ⋁"), bstack11ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥ⋂")]:
        return
    if (str(skipSessionName).lower() != bstack11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⋃")):
        bstack1ll11lll11_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ⋄")))
    bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"ࠦࠧ⋅")
    bstack11l111ll111_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l11l1111l_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧ⋆").format(e)
                )
        try:
            if passed:
                bstack111l1l1lll_opy_(getattr(item, bstack11ll_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬ⋇"), None), bstack11ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ⋈"))
            else:
                error_message = bstack11ll_opy_ (u"ࠨࠩ⋉")
                if bstack1l11l1111l_opy_:
                    bstack11l11l1l1l_opy_(item._page, str(bstack1l11l1111l_opy_), bstack11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ⋊"))
                    bstack111l1l1lll_opy_(getattr(item, bstack11ll_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⋋"), None), bstack11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ⋌"), str(bstack1l11l1111l_opy_))
                    error_message = str(bstack1l11l1111l_opy_)
                else:
                    bstack111l1l1lll_opy_(getattr(item, bstack11ll_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫ⋍"), None), bstack11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ⋎"))
                bstack1lll1ll111l1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦ⋏").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11ll_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ⋐"), default=bstack11ll_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣ⋑"), help=bstack11ll_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤ⋒"))
    parser.addoption(bstack11ll_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ⋓"), default=bstack11ll_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ⋔"), help=bstack11ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ⋕"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11ll_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤ⋖"), action=bstack11ll_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢ⋗"), default=bstack11ll_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤ⋘"),
                         help=bstack11ll_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤ⋙"))
def bstack1ll1llll_opy_(log):
    if not (log[bstack11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⋚")] and log[bstack11ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⋛")].strip()):
        return
    active = bstack1ll11l11_opy_()
    log = {
        bstack11ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⋜"): log[bstack11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⋝")],
        bstack11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⋞"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"ࠩ࡝ࠫ⋟"),
        bstack11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⋠"): log[bstack11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⋡")],
    }
    if active:
        if active[bstack11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⋢")] == bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⋣"):
            log[bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⋤")] = active[bstack11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋥")]
        elif active[bstack11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⋦")] == bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࠨ⋧"):
            log[bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⋨")] = active[bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⋩")]
    bstack1l111l1l_opy_.bstack1l11l1ll_opy_([log])
def bstack1ll11l11_opy_():
    if len(store[bstack11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⋪")]) > 0 and store[bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⋫")][-1]:
        return {
            bstack11ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭⋬"): bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⋭"),
            bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⋮"): store[bstack11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⋯")][-1]
        }
    if store.get(bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⋰"), None):
        return {
            bstack11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋱"): bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࠬ⋲"),
            bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋳"): store[bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⋴")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.INIT_TEST, bstack1lll1ll111l_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.INIT_TEST, bstack1lll1ll111l_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1ll1l1ll_opy_ = True
        bstack1ll1l11lll_opy_ = bstack1111ll11_opy_.bstack11l11lll1_opy_(bstack111l11lllll_opy_(item.own_markers))
        if not cli.bstack1l1l111l1l1_opy_(bstack1l1l11l1ll1_opy_):
            item._a11y_test_case = bstack1ll1l11lll_opy_
            if bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⋵"), None):
                driver = getattr(item, bstack11ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⋶"), None)
                item._a11y_started = bstack1111ll11_opy_.bstack1ll11lll1_opy_(driver, bstack1ll1l11lll_opy_)
        if not bstack1l111l1l_opy_.on() or bstack1lll1llllll1_opy_ != bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⋷"):
            return
        global current_test_uuid #, bstack11lll1ll_opy_
        bstack1lll1lll_opy_ = {
            bstack11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⋸"): uuid4().__str__(),
            bstack11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⋹"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"ࠨ࡜ࠪ⋺")
        }
        current_test_uuid = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋻")]
        store[bstack11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⋼")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⋽")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l1111ll_opy_[item.nodeid] = {**_1l1111ll_opy_[item.nodeid], **bstack1lll1lll_opy_}
        bstack1lll1lllll11_opy_(item, _1l1111ll_opy_[item.nodeid], bstack11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭⋾"))
    except Exception as err:
        print(bstack11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨ⋿"), str(err))
def pytest_runtest_setup(item):
    store[bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⌀")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.PRE, item, bstack11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⌁"))
    if bstack111ll1ll_opy_.bstack11l11111l1l_opy_():
            bstack1lll1ll1llll_opy_ = bstack11ll_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡤࡷࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨ⌂")
            logger.error(bstack1lll1ll1llll_opy_)
            bstack1lll1lll_opy_ = {
                bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⌃"): uuid4().__str__(),
                bstack11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⌄"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"ࠬࡠࠧ⌅"),
                bstack11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⌆"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"࡛ࠧࠩ⌇"),
                bstack11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⌈"): bstack11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⌉"),
                bstack11ll_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ⌊"): bstack1lll1ll1llll_opy_,
                bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⌋"): [],
                bstack11ll_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⌌"): []
            }
            bstack1lll1lllll11_opy_(item, bstack1lll1lll_opy_, bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⌍"))
            pytest.skip(bstack1lll1ll1llll_opy_)
            return # skip all existing operations
    global bstack1lll1lll1ll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack1111ll1l1ll_opy_():
        atexit.register(bstack111llll1l1_opy_)
        if not bstack1lll1lll1ll1_opy_:
            try:
                bstack1lll1ll1111l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111l1111111_opy_():
                    bstack1lll1ll1111l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1ll1111l_opy_:
                    signal.signal(s, bstack1lll1ll1l1l1_opy_)
                bstack1lll1lll1ll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣ⌎") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111l1l11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⌏")
    try:
        if not bstack1l111l1l_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1lll1lll_opy_ = {
            bstack11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌐"): uuid,
            bstack11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⌑"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"ࠫ࡟࠭⌒"),
            bstack11ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⌓"): bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⌔"),
            bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⌕"): bstack11ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭⌖"),
            bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⌗"): bstack11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⌘")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⌙")] = item
        store[bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⌚")] = [uuid]
        if not _1l1111ll_opy_.get(item.nodeid, None):
            _1l1111ll_opy_[item.nodeid] = {bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⌛"): [], bstack11ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌜"): []}
        _1l1111ll_opy_[item.nodeid][bstack11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⌝")].append(bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⌞")])
        _1l1111ll_opy_[item.nodeid + bstack11ll_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪ⌟")] = bstack1lll1lll_opy_
        bstack1lll1lll11ll_opy_(item, bstack1lll1lll_opy_, bstack11ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⌠"))
    except Exception as err:
        print(bstack11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ⌡"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.AFTER_EACH, bstack1lll1ll111l_opy_.PRE, item, bstack11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌢"))
        return # skip all existing operations
    try:
        global bstack1llll11ll1_opy_
        bstack1lll111ll1_opy_ = 0
        if bstack11l111ll1l_opy_ is True:
            bstack1lll111ll1_opy_ = int(os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⌣")))
        if bstack111l1l1ll1_opy_.bstack1l1llll1l1_opy_() == bstack11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨ⌤"):
            if bstack111l1l1ll1_opy_.bstack11111lllll_opy_() == bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ⌥"):
                bstack1lll1llll1l1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⌦"), None)
                bstack111ll11l1_opy_ = bstack1lll1llll1l1_opy_ + bstack11ll_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ⌧")
                driver = getattr(item, bstack11ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⌨"), None)
                bstack1ll11l111l_opy_ = getattr(item, bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ〈"), None)
                bstack111l1111l1_opy_ = getattr(item, bstack11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ〉"), None)
                PercySDK.screenshot(driver, bstack111ll11l1_opy_, bstack1ll11l111l_opy_=bstack1ll11l111l_opy_, bstack111l1111l1_opy_=bstack111l1111l1_opy_, bstack1ll111lll1_opy_=bstack1lll111ll1_opy_)
        if not cli.bstack1l1l111l1l1_opy_(bstack1l1l11l1ll1_opy_):
            if getattr(item, bstack11ll_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨ⌫"), False):
                bstack1lll11lll_opy_.bstack11111111_opy_(getattr(item, bstack11ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⌬"), None), bstack1llll11ll1_opy_, logger, item)
        if not bstack1l111l1l_opy_.on():
            return
        bstack1lll1lll_opy_ = {
            bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⌭"): uuid4().__str__(),
            bstack11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⌮"): bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"ࠬࡠࠧ⌯"),
            bstack11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ⌰"): bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ⌱"),
            bstack11ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⌲"): bstack11ll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭⌳"),
            bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭⌴"): bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⌵")
        }
        _1l1111ll_opy_[item.nodeid + bstack11ll_opy_ (u"ࠬ࠳ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌶")] = bstack1lll1lll_opy_
        bstack1lll1lll11ll_opy_(item, bstack1lll1lll_opy_, bstack11ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⌷"))
    except Exception as err:
        print(bstack11ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯࠼ࠣࡿࢂ࠭⌸"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111l1l1l_opy_(fixturedef.argname):
        store[bstack11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ⌹")] = request.node
    elif bstack11l111ll1ll_opy_(fixturedef.argname):
        store[bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧ⌺")] = request.node
    if not bstack1l111l1l_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1lll1ll111l_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1lll1ll111l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1lll1ll111l_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.SETUP_FIXTURE, bstack1lll1ll111l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ⌻"): fixturedef.argname,
            bstack11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⌼"): bstack1111l1ll111_opy_(outcome),
            bstack11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⌽"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⌾")]
        if not _1l1111ll_opy_.get(current_test_item.nodeid, None):
            _1l1111ll_opy_[current_test_item.nodeid] = {bstack11ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⌿"): []}
        _1l1111ll_opy_[current_test_item.nodeid][bstack11ll_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⍀")].append(fixture)
    except Exception as err:
        logger.debug(bstack11ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬ⍁"), str(err))
if bstack11l1llll1l_opy_() and bstack1l111l1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1lll1ll111l_opy_.PRE, request, step)
            return
        try:
            _1l1111ll_opy_[request.node.nodeid][bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⍂")].bstack11l11lll_opy_(id(step))
        except Exception as err:
            print(bstack11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ⍃"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1lll1ll111l_opy_.POST, request, step, exception)
            return
        try:
            _1l1111ll_opy_[request.node.nodeid][bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⍄")].bstack1l111lll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪ⍅"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.STEP, bstack1lll1ll111l_opy_.POST, request, step)
            return
        try:
            bstack1l11ll1l_opy_: bstack1l1l1l11_opy_ = _1l1111ll_opy_[request.node.nodeid][bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⍆")]
            bstack1l11ll1l_opy_.bstack1l111lll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬ⍇"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1llllll1_opy_
        try:
            if not bstack1l111l1l_opy_.on() or bstack1lll1llllll1_opy_ != bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭⍈"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE, request, feature, scenario)
                return
            driver = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ⍉"), None)
            if not _1l1111ll_opy_.get(request.node.nodeid, None):
                _1l1111ll_opy_[request.node.nodeid] = {}
            bstack1l11ll1l_opy_ = bstack1l1l1l11_opy_.bstack111111l11ll_opy_(
                scenario, feature, request.node,
                name=bstack11l111ll11l_opy_(request.node, scenario),
                started_at=bstack1lll1111_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11ll_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭⍊"),
                tags=bstack11l111l111l_opy_(feature, scenario),
                bstack1l1ll111_opy_=bstack1l111l1l_opy_.bstack1l1lll1l_opy_(driver) if driver and driver.session_id else {}
            )
            _1l1111ll_opy_[request.node.nodeid][bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⍋")] = bstack1l11ll1l_opy_
            bstack1lll1ll11ll1_opy_(bstack1l11ll1l_opy_.uuid)
            bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⍌"), bstack1l11ll1l_opy_)
        except Exception as err:
            print(bstack11ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ⍍"), str(err))
def bstack1lll1ll111ll_opy_(bstack11l11l1l_opy_):
    if bstack11l11l1l_opy_ in store[bstack11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⍎")]:
        store[bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⍏")].remove(bstack11l11l1l_opy_)
def bstack1lll1ll11ll1_opy_(test_uuid):
    store[bstack11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⍐")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l111l1l_opy_.bstack1llll11l11ll_opy_
def bstack1lll1ll1lll1_opy_(item, call, report):
    logger.debug(bstack11ll_opy_ (u"ࠫ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡴࡶࡤࡶࡹ࠭⍑"))
    global bstack1lll1llllll1_opy_
    bstack1ll1l1llll_opy_ = bstack1lll1111_opy_()
    if hasattr(report, bstack11ll_opy_ (u"ࠬࡹࡴࡰࡲࠪ⍒")):
        bstack1ll1l1llll_opy_ = bstack1111llll11l_opy_(report.stop)
    elif hasattr(report, bstack11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࠬ⍓")):
        bstack1ll1l1llll_opy_ = bstack1111llll11l_opy_(report.start)
    try:
        if getattr(report, bstack11ll_opy_ (u"ࠧࡸࡪࡨࡲࠬ⍔"), bstack11ll_opy_ (u"ࠨࠩ⍕")) == bstack11ll_opy_ (u"ࠩࡦࡥࡱࡲࠧ⍖"):
            logger.debug(bstack11ll_opy_ (u"ࠪ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡳࡵࡣࡷࡩࠥ࠳ࠠࡼࡿ࠯ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠ࠮ࠢࡾࢁࠬ⍗").format(getattr(report, bstack11ll_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍘"), bstack11ll_opy_ (u"ࠬ࠭⍙")).__str__(), bstack1lll1llllll1_opy_))
            if bstack1lll1llllll1_opy_ == bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⍚"):
                _1l1111ll_opy_[item.nodeid][bstack11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⍛")] = bstack1ll1l1llll_opy_
                bstack1lll1lllll11_opy_(item, _1l1111ll_opy_[item.nodeid], bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⍜"), report, call)
                store[bstack11ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭⍝")] = None
            elif bstack1lll1llllll1_opy_ == bstack11ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢ⍞"):
                bstack1l11ll1l_opy_ = _1l1111ll_opy_[item.nodeid][bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍟")]
                bstack1l11ll1l_opy_.set(hooks=_1l1111ll_opy_[item.nodeid].get(bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⍠"), []))
                exception, bstack1l11l11l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11l11l_opy_ = [call.excinfo.exconly(), getattr(report, bstack11ll_opy_ (u"࠭࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠬ⍡"), bstack11ll_opy_ (u"ࠧࠨ⍢"))]
                bstack1l11ll1l_opy_.stop(time=bstack1ll1l1llll_opy_, result=Result(result=getattr(report, bstack11ll_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⍣"), bstack11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⍤")), exception=exception, bstack1l11l11l_opy_=bstack1l11l11l_opy_))
                bstack1l111l1l_opy_.bstack1lll1l11_opy_(bstack11ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⍥"), _1l1111ll_opy_[item.nodeid][bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⍦")])
        elif getattr(report, bstack11ll_opy_ (u"ࠬࡽࡨࡦࡰࠪ⍧"), bstack11ll_opy_ (u"࠭ࠧ⍨")) in [bstack11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭⍩"), bstack11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪ⍪")]:
            logger.debug(bstack11ll_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡶࡨࠤ࠲ࠦࡻࡾ࠮ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦ࠭ࠡࡽࢀࠫ⍫").format(getattr(report, bstack11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍬"), bstack11ll_opy_ (u"ࠫࠬ⍭")).__str__(), bstack1lll1llllll1_opy_))
            bstack1l11l1l1_opy_ = item.nodeid + bstack11ll_opy_ (u"ࠬ࠳ࠧ⍮") + getattr(report, bstack11ll_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍯"), bstack11ll_opy_ (u"ࠧࠨ⍰"))
            if getattr(report, bstack11ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ⍱"), False):
                hook_type = bstack11ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ⍲") if getattr(report, bstack11ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⍳"), bstack11ll_opy_ (u"ࠫࠬ⍴")) == bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⍵") else bstack11ll_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ⍶")
                _1l1111ll_opy_[bstack1l11l1l1_opy_] = {
                    bstack11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⍷"): uuid4().__str__(),
                    bstack11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⍸"): bstack1ll1l1llll_opy_,
                    bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⍹"): hook_type
                }
            _1l1111ll_opy_[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⍺")] = bstack1ll1l1llll_opy_
            bstack1lll1ll111ll_opy_(_1l1111ll_opy_[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⍻")])
            bstack1lll1lll11ll_opy_(item, _1l1111ll_opy_[bstack1l11l1l1_opy_], bstack11ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⍼"), report, call)
            if getattr(report, bstack11ll_opy_ (u"࠭ࡷࡩࡧࡱࠫ⍽"), bstack11ll_opy_ (u"ࠧࠨ⍾")) == bstack11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⍿"):
                if getattr(report, bstack11ll_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ⎀"), bstack11ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⎁")) == bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⎂"):
                    bstack1lll1lll_opy_ = {
                        bstack11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ⎃"): uuid4().__str__(),
                        bstack11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⎄"): bstack1lll1111_opy_(),
                        bstack11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎅"): bstack1lll1111_opy_()
                    }
                    _1l1111ll_opy_[item.nodeid] = {**_1l1111ll_opy_[item.nodeid], **bstack1lll1lll_opy_}
                    bstack1lll1lllll11_opy_(item, _1l1111ll_opy_[item.nodeid], bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⎆"))
                    bstack1lll1lllll11_opy_(item, _1l1111ll_opy_[item.nodeid], bstack11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⎇"), report, call)
    except Exception as err:
        print(bstack11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨ⎈"), str(err))
def bstack1lll1lllll1l_opy_(test, bstack1lll1lll_opy_, result=None, call=None, bstack11l11111l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l11ll1l_opy_ = {
        bstack11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⎉"): bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ⎊")],
        bstack11ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ⎋"): bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࠬ⎌"),
        bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭⎍"): test.name,
        bstack11ll_opy_ (u"ࠩࡥࡳࡩࡿࠧ⎎"): {
            bstack11ll_opy_ (u"ࠪࡰࡦࡴࡧࠨ⎏"): bstack11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ⎐"),
            bstack11ll_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ⎑"): inspect.getsource(test.obj)
        },
        bstack11ll_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ⎒"): test.name,
        bstack11ll_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭⎓"): test.name,
        bstack11ll_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨ⎔"): bstack1l1l111l_opy_.bstack1l11ll11_opy_(test),
        bstack11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ⎕"): file_path,
        bstack11ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬ⎖"): file_path,
        bstack11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎗"): bstack11ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⎘"),
        bstack11ll_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫ⎙"): file_path,
        bstack11ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⎚"): bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⎛")],
        bstack11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ⎜"): bstack11ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪ⎝"),
        bstack11ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧ⎞"): {
            bstack11ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩ⎟"): test.nodeid
        },
        bstack11ll_opy_ (u"࠭ࡴࡢࡩࡶࠫ⎠"): bstack111l11lllll_opy_(test.own_markers)
    }
    if bstack11l11111l_opy_ in [bstack11ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ⎡"), bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⎢")]:
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠩࡰࡩࡹࡧࠧ⎣")] = {
            bstack11ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⎤"): bstack1lll1lll_opy_.get(bstack11ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭⎥"), [])
        }
    if bstack11l11111l_opy_ == bstack11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⎦"):
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎧")] = bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⎨")
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎩")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎪")]
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎫")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎬")]
    if result:
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎭")] = result.outcome
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⎮")] = result.duration * 1000
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎯")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎰")]
        if result.failed:
            bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⎱")] = bstack1l111l1l_opy_.bstack1111111ll1_opy_(call.excinfo.typename)
            bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⎲")] = bstack1l111l1l_opy_.bstack1llll111llll_opy_(call.excinfo, result)
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⎳")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⎴")]
    if outcome:
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⎵")] = bstack1111l1ll111_opy_(outcome)
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⎶")] = 0
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⎷")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎸")]
        if bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎹")] == bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⎺"):
            bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⎻")] = bstack11ll_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ⎼")  # bstack1lll1lll1lll_opy_
            bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⎽")] = [{bstack11ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⎾"): [bstack11ll_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭⎿")]}]
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⏀")] = bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⏁")]
    return bstack1l11ll1l_opy_
def bstack1lll1lll111l_opy_(test, bstack11lll11l_opy_, bstack11l11111l_opy_, result, call, outcome, bstack1lll1lll1l11_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⏂")]
    hook_name = bstack11lll11l_opy_[bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ⏃")]
    hook_data = {
        bstack11ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⏄"): bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⏅")],
        bstack11ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⏆"): bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ⏇"),
        bstack11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⏈"): bstack11ll_opy_ (u"ࠬࢁࡽࠨ⏉").format(bstack11l111l1ll1_opy_(hook_name)),
        bstack11ll_opy_ (u"࠭ࡢࡰࡦࡼࠫ⏊"): {
            bstack11ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬ⏋"): bstack11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⏌"),
            bstack11ll_opy_ (u"ࠩࡦࡳࡩ࡫ࠧ⏍"): None
        },
        bstack11ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩ⏎"): test.name,
        bstack11ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫ⏏"): bstack1l1l111l_opy_.bstack1l11ll11_opy_(test, hook_name),
        bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ⏐"): file_path,
        bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ⏑"): file_path,
        bstack11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏒"): bstack11ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⏓"),
        bstack11ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ⏔"): file_path,
        bstack11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⏕"): bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⏖")],
        bstack11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⏗"): bstack11ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ⏘") if bstack1lll1llllll1_opy_ == bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⏙") else bstack11ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ⏚"),
        bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ⏛"): hook_type
    }
    bstack1l1111l1l11_opy_ = bstack1ll11ll1_opy_(_1l1111ll_opy_.get(test.nodeid, None))
    if bstack1l1111l1l11_opy_:
        hook_data[bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨ⏜")] = bstack1l1111l1l11_opy_
    if result:
        hook_data[bstack11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏝")] = result.outcome
        hook_data[bstack11ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⏞")] = result.duration * 1000
        hook_data[bstack11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏟")] = bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⏠")]
        if result.failed:
            hook_data[bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏡")] = bstack1l111l1l_opy_.bstack1111111ll1_opy_(call.excinfo.typename)
            hook_data[bstack11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⏢")] = bstack1l111l1l_opy_.bstack1llll111llll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⏣")] = bstack1111l1ll111_opy_(outcome)
        hook_data[bstack11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⏤")] = 100
        hook_data[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏥")] = bstack11lll11l_opy_[bstack11ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⏦")]
        if hook_data[bstack11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏧")] == bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⏨"):
            hook_data[bstack11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ⏩")] = bstack11ll_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫ⏪")  # bstack1lll1lll1lll_opy_
            hook_data[bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬ⏫")] = [{bstack11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨ⏬"): [bstack11ll_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪ⏭")]}]
    if bstack1lll1lll1l11_opy_:
        hook_data[bstack11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⏮")] = bstack1lll1lll1l11_opy_.result
        hook_data[bstack11ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⏯")] = bstack111l111lll1_opy_(bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⏰")], bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏱")])
        hook_data[bstack11ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏲")] = bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⏳")]
        if hook_data[bstack11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⏴")] == bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⏵"):
            hook_data[bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⏶")] = bstack1l111l1l_opy_.bstack1111111ll1_opy_(bstack1lll1lll1l11_opy_.exception_type)
            hook_data[bstack11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⏷")] = [{bstack11ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭⏸"): bstack111l11lll1l_opy_(bstack1lll1lll1l11_opy_.exception)}]
    return hook_data
def bstack1lll1lllll11_opy_(test, bstack1lll1lll_opy_, bstack11l11111l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11ll_opy_ (u"ࠫࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡴࡦࡵࡷࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠣ࠱ࠥࢁࡽࠨ⏹").format(bstack11l11111l_opy_))
    bstack1l11ll1l_opy_ = bstack1lll1lllll1l_opy_(test, bstack1lll1lll_opy_, result, call, bstack11l11111l_opy_, outcome)
    driver = getattr(test, bstack11ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭⏺"), None)
    if bstack11l11111l_opy_ == bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⏻") and driver:
        bstack1l11ll1l_opy_[bstack11ll_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭⏼")] = bstack1l111l1l_opy_.bstack1l1lll1l_opy_(driver)
    if bstack11l11111l_opy_ == bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ⏽"):
        bstack11l11111l_opy_ = bstack11ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⏾")
    bstack1l11l111_opy_ = {
        bstack11ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⏿"): bstack11l11111l_opy_,
        bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭␀"): bstack1l11ll1l_opy_
    }
    bstack1l111l1l_opy_.bstack1ll1lll1_opy_(bstack1l11l111_opy_)
    if bstack11l11111l_opy_ == bstack11ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭␁"):
        threading.current_thread().bstackTestMeta = {bstack11ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭␂"): bstack11ll_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ␃")}
    elif bstack11l11111l_opy_ == bstack11ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ␄"):
        threading.current_thread().bstackTestMeta = {bstack11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ␅"): getattr(result, bstack11ll_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫ␆"), bstack11ll_opy_ (u"ࠫࠬ␇"))}
def bstack1lll1lll11ll_opy_(test, bstack1lll1lll_opy_, bstack11l11111l_opy_, result=None, call=None, outcome=None, bstack1lll1lll1l11_opy_=None):
    logger.debug(bstack11ll_opy_ (u"ࠬࡹࡥ࡯ࡦࡢ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡩࡱࡲ࡯ࠥࡪࡡࡵࡣ࠯ࠤࡪࡼࡥ࡯ࡶࡗࡽࡵ࡫ࠠ࠮ࠢࡾࢁࠬ␈").format(bstack11l11111l_opy_))
    hook_data = bstack1lll1lll111l_opy_(test, bstack1lll1lll_opy_, bstack11l11111l_opy_, result, call, outcome, bstack1lll1lll1l11_opy_)
    bstack1l11l111_opy_ = {
        bstack11ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ␉"): bstack11l11111l_opy_,
        bstack11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩ␊"): hook_data
    }
    bstack1l111l1l_opy_.bstack1ll1lll1_opy_(bstack1l11l111_opy_)
def bstack1ll11ll1_opy_(bstack1lll1lll_opy_):
    if not bstack1lll1lll_opy_:
        return None
    if bstack1lll1lll_opy_.get(bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ␋"), None):
        return getattr(bstack1lll1lll_opy_[bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ␌")], bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ␍"), None)
    return bstack1lll1lll_opy_.get(bstack11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ␎"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG, bstack1lll1ll111l_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_.LOG, bstack1lll1ll111l_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1l111l1l_opy_.on():
            return
        places = [bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ␏"), bstack11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ␐"), bstack11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ␑")]
        logs = []
        for bstack1lll1lll1111_opy_ in places:
            records = caplog.get_records(bstack1lll1lll1111_opy_)
            bstack1lll1llll111_opy_ = bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ␒") if bstack1lll1lll1111_opy_ == bstack11ll_opy_ (u"ࠩࡦࡥࡱࡲࠧ␓") else bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ␔")
            bstack1llll1111111_opy_ = request.node.nodeid + (bstack11ll_opy_ (u"ࠫࠬ␕") if bstack1lll1lll1111_opy_ == bstack11ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ␖") else bstack11ll_opy_ (u"࠭࠭ࠨ␗") + bstack1lll1lll1111_opy_)
            test_uuid = bstack1ll11ll1_opy_(_1l1111ll_opy_.get(bstack1llll1111111_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack1111l1lllll_opy_(record.message):
                    continue
                logs.append({
                    bstack11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ␘"): bstack111l111l1l1_opy_(record.created).isoformat() + bstack11ll_opy_ (u"ࠨ࡜ࠪ␙"),
                    bstack11ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ␚"): record.levelname,
                    bstack11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ␛"): record.message,
                    bstack1lll1llll111_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l111l1l_opy_.bstack1l11l1ll_opy_(logs)
    except Exception as err:
        print(bstack11ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ␜"), str(err))
def bstack11llllll11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1ll11l11l_opy_
    bstack11l111l1l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ␝"), None) and bstack1l1l11l1_opy_(
            threading.current_thread(), bstack11ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ␞"), None)
    bstack111lllll1l_opy_ = getattr(driver, bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ␟"), None) != None and getattr(driver, bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ␠"), None) == True
    if sequence == bstack11ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ␡") and driver != None:
      if not bstack1ll11l11l_opy_ and bstack1lll1l1ll1l_opy_() and bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ␢") in CONFIG and CONFIG[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ␣")] == True and bstack1l1l1l1l1_opy_.bstack11111l1ll_opy_(driver_command) and (bstack111lllll1l_opy_ or bstack11l111l1l_opy_) and not bstack1llllll111_opy_(args):
        try:
          bstack1ll11l11l_opy_ = True
          logger.debug(bstack11ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧ␤").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫ␥").format(str(err)))
        bstack1ll11l11l_opy_ = False
    if sequence == bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭␦"):
        if driver_command == bstack11ll_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ␧"):
            bstack1l111l1l_opy_.bstack1l1l11lll_opy_({
                bstack11ll_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ␨"): response[bstack11ll_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ␩")],
                bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ␪"): store[bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ␫")]
            })
def bstack111llll1l1_opy_():
    global bstack1111lll1l_opy_
    bstack11l1l1l1ll_opy_.bstack111lll11ll_opy_()
    logging.shutdown()
    bstack1l111l1l_opy_.bstack1l1l1111_opy_()
    for driver in bstack1111lll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1ll1l1l1_opy_(*args):
    global bstack1111lll1l_opy_
    bstack1l111l1l_opy_.bstack1l1l1111_opy_()
    for driver in bstack1111lll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111llllll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11lllll11_opy_(self, *args, **kwargs):
    bstack1l1lll1l11_opy_ = bstack11ll111l1_opy_(self, *args, **kwargs)
    bstack11ll11l1ll_opy_ = getattr(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ␬"), None)
    if bstack11ll11l1ll_opy_ and bstack11ll11l1ll_opy_.get(bstack11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ␭"), bstack11ll_opy_ (u"ࠨࠩ␮")) == bstack11ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ␯"):
        bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
    return bstack1l1lll1l11_opy_
@measure(event_name=EVENTS.bstack11l1l1lll1_opy_, stage=STAGE.bstack1l1lll1lll_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11l1l11ll1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
    if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ␰")):
        return
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ␱"), True)
    global bstack11l11l111l_opy_
    global bstack1ll1ll11l_opy_
    bstack11l11l111l_opy_ = framework_name
    logger.info(bstack11l1111111_opy_.format(bstack11l11l111l_opy_.split(bstack11ll_opy_ (u"ࠬ࠳ࠧ␲"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1lll1l1ll1l_opy_():
            Service.start = bstack1l111ll1l_opy_
            Service.stop = bstack1l1111llll_opy_
            webdriver.Remote.get = bstack11llll1111_opy_
            webdriver.Remote.__init__ = bstack1lll11ll11_opy_
            if not isinstance(os.getenv(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ␳")), str):
                return
            WebDriver.quit = bstack11ll11ll11_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l111l1l_opy_.on():
            webdriver.Remote.__init__ = bstack11lllll11_opy_
        bstack1ll1ll11l_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11ll_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬ␴")):
        bstack1ll1ll11l_opy_ = eval(os.environ.get(bstack11ll_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭␵")))
    if not bstack1ll1ll11l_opy_:
        bstack1lll11llll_opy_(bstack11ll_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ␶"), bstack11l1111l1l_opy_)
    if bstack11lll111l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11ll_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ␷")) and callable(getattr(RemoteConnection, bstack11ll_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ␸"))):
                RemoteConnection._get_proxy_url = bstack11111ll11l_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack11111ll11l_opy_
        except Exception as e:
            logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
    if bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ␹") in str(framework_name).lower():
        if not bstack1lll1l1ll1l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1l1llll11l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1ll11ll_opy_
            Config.getoption = bstack111l1ll1l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1l11ll_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll1llll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11ll11ll11_opy_(self):
    global bstack11l11l111l_opy_
    global bstack1l1ll1111l_opy_
    global bstack1l111lllll_opy_
    try:
        if bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭␺") in bstack11l11l111l_opy_ and self.session_id != None and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ␻"), bstack11ll_opy_ (u"ࠨࠩ␼")) != bstack11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ␽"):
            bstack11l11l1ll1_opy_ = bstack11ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ␾") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ␿")
            bstack11111l111l_opy_(logger, True)
            if os.environ.get(bstack11ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ⑀"), None):
                self.execute_script(
                    bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ⑁") + json.dumps(
                        os.environ.get(bstack11ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ⑂"))) + bstack11ll_opy_ (u"ࠨࡿࢀࠫ⑃"))
            if self != None:
                bstack1ll1111111_opy_(self, bstack11l11l1ll1_opy_, bstack11ll_opy_ (u"ࠩ࠯ࠤࠬ⑄").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1l111l1l1_opy_(bstack1l1l11l1ll1_opy_):
            item = store.get(bstack11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⑅"), None)
            if item is not None and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ⑆"), None):
                bstack1lll11lll_opy_.bstack11111111_opy_(self, bstack1llll11ll1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11ll_opy_ (u"ࠬ࠭⑇")
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢ⑈") + str(e))
    bstack1l111lllll_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1ll1l1lll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1lll11ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l1ll1111l_opy_
    global bstack1111llll1_opy_
    global bstack11l111ll1l_opy_
    global bstack11l11l111l_opy_
    global bstack11ll111l1_opy_
    global bstack1111lll1l_opy_
    global bstack1lllll1l11_opy_
    global bstack111l1l11l_opy_
    global bstack1llll11ll1_opy_
    CONFIG[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ⑉")] = str(bstack11l11l111l_opy_) + str(__version__)
    command_executor = bstack1lll11lll1_opy_(bstack1lllll1l11_opy_, CONFIG)
    logger.debug(bstack1lll1lllll_opy_.format(command_executor))
    proxy = bstack11l1lll1l_opy_(CONFIG, proxy)
    bstack1lll111ll1_opy_ = 0
    try:
        if bstack11l111ll1l_opy_ is True:
            bstack1lll111ll1_opy_ = int(os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⑊")))
    except:
        bstack1lll111ll1_opy_ = 0
    bstack111l11ll11_opy_ = bstack1l1lllll11_opy_(CONFIG, bstack1lll111ll1_opy_)
    logger.debug(bstack11llll111_opy_.format(str(bstack111l11ll11_opy_)))
    bstack1llll11ll1_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑋"))[bstack1lll111ll1_opy_]
    if bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⑌") in CONFIG and CONFIG[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ⑍")]:
        bstack1lll1ll1ll_opy_(bstack111l11ll11_opy_, bstack111l1l11l_opy_)
    if bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1lll111ll1_opy_) and bstack1111ll11_opy_.bstack11ll1l1l1_opy_(bstack111l11ll11_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1l111l1l1_opy_(bstack1l1l11l1ll1_opy_):
            bstack1111ll11_opy_.set_capabilities(bstack111l11ll11_opy_, CONFIG)
    if desired_capabilities:
        bstack111111l1l_opy_ = bstack1111lll1l1_opy_(desired_capabilities)
        bstack111111l1l_opy_[bstack11ll_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ⑎")] = bstack1l11l1l1l_opy_(CONFIG)
        bstack111llll11l_opy_ = bstack1l1lllll11_opy_(bstack111111l1l_opy_)
        if bstack111llll11l_opy_:
            bstack111l11ll11_opy_ = update(bstack111llll11l_opy_, bstack111l11ll11_opy_)
        desired_capabilities = None
    if options:
        bstack1l11l1l1l1_opy_(options, bstack111l11ll11_opy_)
    if not options:
        options = bstack1111111l1_opy_(bstack111l11ll11_opy_)
    if proxy and bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭⑏")):
        options.proxy(proxy)
    if options and bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭⑐")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11l11l11l1_opy_() < version.parse(bstack11ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ⑑")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack111l11ll11_opy_)
    logger.info(bstack1ll1lll1ll_opy_)
    bstack11l1l1ll11_opy_.end(EVENTS.bstack11l1l1lll1_opy_.value, EVENTS.bstack11l1l1lll1_opy_.value + bstack11ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ⑒"),
                               EVENTS.bstack11l1l1lll1_opy_.value + bstack11ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ⑓"), True, None)
    try:
        if bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ⑔")):
            bstack11ll111l1_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ⑕")):
            bstack11ll111l1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭⑖")):
            bstack11ll111l1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack11ll111l1_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack11ll1lllll_opy_:
        logger.error(bstack11111l11ll_opy_.format(bstack11ll_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭⑗"), str(bstack11ll1lllll_opy_)))
        raise bstack11ll1lllll_opy_
    try:
        bstack1l111111l_opy_ = bstack11ll_opy_ (u"ࠨࠩ⑘")
        if bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪ⑙")):
            bstack1l111111l_opy_ = self.caps.get(bstack11ll_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ⑚"))
        else:
            bstack1l111111l_opy_ = self.capabilities.get(bstack11ll_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ⑛"))
        if bstack1l111111l_opy_:
            bstack11111l1l1l_opy_(bstack1l111111l_opy_)
            if bstack11l11l11l1_opy_() <= version.parse(bstack11ll_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ⑜")):
                self.command_executor._url = bstack11ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ⑝") + bstack1lllll1l11_opy_ + bstack11ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ⑞")
            else:
                self.command_executor._url = bstack11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ⑟") + bstack1l111111l_opy_ + bstack11ll_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ①")
            logger.debug(bstack1l1l1l1l1l_opy_.format(bstack1l111111l_opy_))
        else:
            logger.debug(bstack1l11ll111l_opy_.format(bstack11ll_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ②")))
    except Exception as e:
        logger.debug(bstack1l11ll111l_opy_.format(e))
    bstack1l1ll1111l_opy_ = self.session_id
    if bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ③") in bstack11l11l111l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ④"), None)
        if item:
            bstack1lll1ll1l11l_opy_ = getattr(item, bstack11ll_opy_ (u"࠭࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࡢࡷࡹࡧࡲࡵࡧࡧࠫ⑤"), False)
            if not getattr(item, bstack11ll_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⑥"), None) and bstack1lll1ll1l11l_opy_:
                setattr(store[bstack11ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ⑦")], bstack11ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⑧"), self)
        bstack11ll11l1ll_opy_ = getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ⑨"), None)
        if bstack11ll11l1ll_opy_ and bstack11ll11l1ll_opy_.get(bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⑩"), bstack11ll_opy_ (u"ࠬ࠭⑪")) == bstack11ll_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⑫"):
            bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
    bstack1111lll1l_opy_.append(self)
    if bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⑬") in CONFIG and bstack11ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⑭") in CONFIG[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑮")][bstack1lll111ll1_opy_]:
        bstack1111llll1_opy_ = CONFIG[bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⑯")][bstack1lll111ll1_opy_][bstack11ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑰")]
    logger.debug(bstack1l1l1l1lll_opy_.format(bstack1l1ll1111l_opy_))
@measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11llll1111_opy_(self, url):
    global bstack11ll1l1111_opy_
    global CONFIG
    try:
        bstack1111l1lll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll11ll111_opy_.format(str(err)))
    try:
        bstack11ll1l1111_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack1l1l1ll1l_opy_):
                bstack1111l1lll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll11ll111_opy_.format(str(err)))
        raise e
def bstack11l111l111_opy_(item, when):
    global bstack11ll111lll_opy_
    try:
        bstack11ll111lll_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1l11ll_opy_(item, call, rep):
    global bstack1ll1l1l11l_opy_
    global bstack1111lll1l_opy_
    name = bstack11ll_opy_ (u"ࠬ࠭⑱")
    try:
        if rep.when == bstack11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ⑲"):
            bstack1l1ll1111l_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ⑳"))
            try:
                if (str(skipSessionName).lower() != bstack11ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭⑴")):
                    name = str(rep.nodeid)
                    bstack1lll1l1l1l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⑵"), name, bstack11ll_opy_ (u"ࠪࠫ⑶"), bstack11ll_opy_ (u"ࠫࠬ⑷"), bstack11ll_opy_ (u"ࠬ࠭⑸"), bstack11ll_opy_ (u"࠭ࠧ⑹"))
                    os.environ[bstack11ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ⑺")] = name
                    for driver in bstack1111lll1l_opy_:
                        if bstack1l1ll1111l_opy_ == driver.session_id:
                            driver.execute_script(bstack1lll1l1l1l_opy_)
            except Exception as e:
                logger.debug(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⑻").format(str(e)))
            try:
                bstack11ll1l11l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ⑼"):
                    status = bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⑽") if rep.outcome.lower() == bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⑾") else bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⑿")
                    reason = bstack11ll_opy_ (u"࠭ࠧ⒀")
                    if status == bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⒁"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11ll_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭⒂") if status == bstack11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ⒃") else bstack11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⒄")
                    data = name + bstack11ll_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭⒅") if status == bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ⒆") else name + bstack11ll_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩ⒇") + reason
                    bstack11l11ll11l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ⒈"), bstack11ll_opy_ (u"ࠨࠩ⒉"), bstack11ll_opy_ (u"ࠩࠪ⒊"), bstack11ll_opy_ (u"ࠪࠫ⒋"), level, data)
                    for driver in bstack1111lll1l_opy_:
                        if bstack1l1ll1111l_opy_ == driver.session_id:
                            driver.execute_script(bstack11l11ll11l_opy_)
            except Exception as e:
                logger.debug(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ⒌").format(str(e)))
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩ⒍").format(str(e)))
    bstack1ll1l1l11l_opy_(item, call, rep)
notset = Notset()
def bstack111l1ll1l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack111l11l1l1_opy_
    if str(name).lower() == bstack11ll_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭⒎"):
        return bstack11ll_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ⒏")
    else:
        return bstack111l11l1l1_opy_(self, name, default, skip)
def bstack11111ll11l_opy_(self):
    global CONFIG
    global bstack1l11ll1l11_opy_
    try:
        proxy = bstack111lll1l1l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11ll_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭⒐")):
                proxies = bstack111ll1l1ll_opy_(proxy, bstack1lll11lll1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1111111_opy_ = proxies.popitem()
                    if bstack11ll_opy_ (u"ࠤ࠽࠳࠴ࠨ⒑") in bstack1l1111111_opy_:
                        return bstack1l1111111_opy_
                    else:
                        return bstack11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ⒒") + bstack1l1111111_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ⒓").format(str(e)))
    return bstack1l11ll1l11_opy_(self)
def bstack11lll111l_opy_():
    return (bstack11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ⒔") in CONFIG or bstack11ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ⒕") in CONFIG) and bstack11llll1l1l_opy_() and bstack11l11l11l1_opy_() >= version.parse(
        bstack11l1l1l111_opy_)
def bstack111l111l1_opy_(self,
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
    global bstack1111llll1_opy_
    global bstack11l111ll1l_opy_
    global bstack11l11l111l_opy_
    CONFIG[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ⒖")] = str(bstack11l11l111l_opy_) + str(__version__)
    bstack1lll111ll1_opy_ = 0
    try:
        if bstack11l111ll1l_opy_ is True:
            bstack1lll111ll1_opy_ = int(os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ⒗")))
    except:
        bstack1lll111ll1_opy_ = 0
    CONFIG[bstack11ll_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ⒘")] = True
    bstack111l11ll11_opy_ = bstack1l1lllll11_opy_(CONFIG, bstack1lll111ll1_opy_)
    logger.debug(bstack11llll111_opy_.format(str(bstack111l11ll11_opy_)))
    if CONFIG.get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ⒙")):
        bstack1lll1ll1ll_opy_(bstack111l11ll11_opy_, bstack111l1l11l_opy_)
    if bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⒚") in CONFIG and bstack11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ⒛") in CONFIG[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⒜")][bstack1lll111ll1_opy_]:
        bstack1111llll1_opy_ = CONFIG[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⒝")][bstack1lll111ll1_opy_][bstack11ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭⒞")]
    import urllib
    import json
    if bstack11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⒟") in CONFIG and str(CONFIG[bstack11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ⒠")]).lower() != bstack11ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ⒡"):
        bstack1l1l11111_opy_ = bstack1l1l1111ll_opy_()
        bstack11l1l111l_opy_ = bstack1l1l11111_opy_ + urllib.parse.quote(json.dumps(bstack111l11ll11_opy_))
    else:
        bstack11l1l111l_opy_ = bstack11ll_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧ⒢") + urllib.parse.quote(json.dumps(bstack111l11ll11_opy_))
    browser = self.connect(bstack11l1l111l_opy_)
    return browser
def bstack11lll111l1_opy_():
    global bstack1ll1ll11l_opy_
    global bstack11l11l111l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111ll1ll1_opy_
        if not bstack1lll1l1ll1l_opy_():
            global bstack11lll1l11_opy_
            if not bstack11lll1l11_opy_:
                from bstack_utils.helper import bstack1ll111l11_opy_, bstack1l1l11ll1_opy_
                bstack11lll1l11_opy_ = bstack1ll111l11_opy_()
                bstack1l1l11ll1_opy_(bstack11l11l111l_opy_)
            BrowserType.connect = bstack1111ll1ll1_opy_
            return
        BrowserType.launch = bstack111l111l1_opy_
        bstack1ll1ll11l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1ll11l11_opy_():
    global CONFIG
    global bstack1l111ll1l1_opy_
    global bstack1lllll1l11_opy_
    global bstack111l1l11l_opy_
    global bstack11l111ll1l_opy_
    global bstack1ll11l1lll_opy_
    CONFIG = json.loads(os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬ⒣")))
    bstack1l111ll1l1_opy_ = eval(os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ⒤")))
    bstack1lllll1l11_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨ⒥"))
    bstack11l111lll_opy_(CONFIG, bstack1l111ll1l1_opy_)
    bstack1ll11l1lll_opy_ = bstack11l1l1l1ll_opy_.configure_logger(CONFIG, bstack1ll11l1lll_opy_)
    if cli.bstack111ll1l11_opy_():
        bstack1111l11l11_opy_.invoke(Events.CONNECT, bstack1l1l11llll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ⒦"), bstack11ll_opy_ (u"ࠪ࠴ࠬ⒧")))
        cli.bstack1l11ll11ll1_opy_(cli_context.platform_index)
        cli.bstack1l1l11l1l1l_opy_(bstack1lll11lll1_opy_(bstack1lllll1l11_opy_, CONFIG), cli_context.platform_index, bstack1111111l1_opy_)
        cli.bstack1l1l1l1l11l_opy_()
        logger.debug(bstack11ll_opy_ (u"ࠦࡈࡒࡉࠡ࡫ࡶࠤࡦࡩࡴࡪࡸࡨࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥ⒨") + str(cli_context.platform_index) + bstack11ll_opy_ (u"ࠧࠨ⒩"))
        return # skip all existing operations
    global bstack11ll111l1_opy_
    global bstack1l111lllll_opy_
    global bstack11l11l1l1_opy_
    global bstack111l111lll_opy_
    global bstack111lll11l1_opy_
    global bstack1ll111111_opy_
    global bstack1l11ll11l_opy_
    global bstack11ll1l1111_opy_
    global bstack1l11ll1l11_opy_
    global bstack111l11l1l1_opy_
    global bstack11ll111lll_opy_
    global bstack1ll1l1l11l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11ll111l1_opy_ = webdriver.Remote.__init__
        bstack1l111lllll_opy_ = WebDriver.quit
        bstack1l11ll11l_opy_ = WebDriver.close
        bstack11ll1l1111_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ⒪") in CONFIG or bstack11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ⒫") in CONFIG) and bstack11llll1l1l_opy_():
        if bstack11l11l11l1_opy_() < version.parse(bstack11l1l1l111_opy_):
            logger.error(bstack1111llllll_opy_.format(bstack11l11l11l1_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11ll_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ⒬")) and callable(getattr(RemoteConnection, bstack11ll_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ⒭"))):
                    bstack1l11ll1l11_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1l11ll1l11_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack111l11l1l1_opy_ = Config.getoption
        from _pytest import runner
        bstack11ll111lll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1lll1l1ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll1l1l11l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ⒮"))
    bstack111l1l11l_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ⒯"), {}).get(bstack11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ⒰"))
    bstack11l111ll1l_opy_ = True
    bstack11l1l11ll1_opy_(bstack11l1ll1111_opy_)
if (bstack1111ll1l1ll_opy_()):
    bstack1lll1ll11l11_opy_()
@error_handler(class_method=False)
def bstack1llll111111l_opy_(hook_name, event, bstack1ll11lll111_opy_=None):
    if hook_name not in [bstack11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ⒱"), bstack11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫ⒲"), bstack11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ⒳"), bstack11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ⒴"), bstack11ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ⒵"), bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬⒶ"), bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫⒷ"), bstack11ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨⒸ")]:
        return
    node = store[bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫⒹ")]
    if hook_name in [bstack11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧⒺ"), bstack11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫⒻ")]:
        node = store[bstack11ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡲࡵࡤࡶ࡮ࡨࡣ࡮ࡺࡥ࡮ࠩⒼ")]
    elif hook_name in [bstack11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩⒽ"), bstack11ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭Ⓘ")]:
        node = store[bstack11ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫⒿ")]
    hook_type = bstack11l111l1lll_opy_(hook_name)
    if event == bstack11ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧⓀ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_[hook_type], bstack1lll1ll111l_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack11lll11l_opy_ = {
            bstack11ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ⓛ"): uuid,
            bstack11ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ⓜ"): bstack1lll1111_opy_(),
            bstack11ll_opy_ (u"ࠪࡸࡾࡶࡥࠨⓃ"): bstack11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩⓄ"),
            bstack11ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨⓅ"): hook_type,
            bstack11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩⓆ"): hook_name
        }
        store[bstack11ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫⓇ")].append(uuid)
        bstack1lll1lll11l1_opy_ = node.nodeid
        if hook_type == bstack11ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭Ⓢ"):
            if not _1l1111ll_opy_.get(bstack1lll1lll11l1_opy_, None):
                _1l1111ll_opy_[bstack1lll1lll11l1_opy_] = {bstack11ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨⓉ"): []}
            _1l1111ll_opy_[bstack1lll1lll11l1_opy_][bstack11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩⓊ")].append(bstack11lll11l_opy_[bstack11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩⓋ")])
        _1l1111ll_opy_[bstack1lll1lll11l1_opy_ + bstack11ll_opy_ (u"ࠬ࠳ࠧⓌ") + hook_name] = bstack11lll11l_opy_
        bstack1lll1lll11ll_opy_(node, bstack11lll11l_opy_, bstack11ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧⓍ"))
    elif event == bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭Ⓨ"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1l1ll11_opy_[hook_type], bstack1lll1ll111l_opy_.POST, node, None, bstack1ll11lll111_opy_)
            return
        bstack1l11l1l1_opy_ = node.nodeid + bstack11ll_opy_ (u"ࠨ࠯ࠪⓏ") + hook_name
        _1l1111ll_opy_[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧⓐ")] = bstack1lll1111_opy_()
        bstack1lll1ll111ll_opy_(_1l1111ll_opy_[bstack1l11l1l1_opy_][bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨⓑ")])
        bstack1lll1lll11ll_opy_(node, _1l1111ll_opy_[bstack1l11l1l1_opy_], bstack11ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ⓒ"), bstack1lll1lll1l11_opy_=bstack1ll11lll111_opy_)
def bstack1lll1ll1l111_opy_():
    global bstack1lll1llllll1_opy_
    if bstack11l1llll1l_opy_():
        bstack1lll1llllll1_opy_ = bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩⓓ")
    else:
        bstack1lll1llllll1_opy_ = bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ⓔ")
def pytest_collection_modifyitems(session, config, items):
    bstack11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡇ࡫࡯ࡸࡪࡸࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡵࡿࡴࡦࡵࡷࠤ࡮ࡺࡥ࡮ࡵࠣࡦࡦࡹࡥࡥࠢࡲࡲࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵࡧࡧࠤࡸ࡫࡬ࡦࡥࡷࡳࡷࡹࠠࡧࡴࡲࡱࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡳࡸࡨࡶ࠳ࠐࠠࠡࠢࠣࠦࠧࠨⓕ")
    import os
    bstack1lll1ll1ll1l_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔࠩⓖ"))
    if not bstack1lll1ll1ll1l_opy_:
        return
    try:
        bstack1lll1llll11l_opy_ = json.loads(bstack1lll1ll1ll1l_opy_)
        if not isinstance(bstack1lll1llll11l_opy_, (list, set)) or not bstack1lll1llll11l_opy_:
            return
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠤࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡶࡡࡳࡵࡨࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡓࡗࡉࡈࡆࡕࡗࡖࡆ࡚ࡅࡅࡡࡖࡉࡑࡋࡃࡕࡑࡕࡗ࠿ࠦࠢⓗ") + str(e) + bstack11ll_opy_ (u"ࠥࠦⓘ"))
        return
    selected = []
    deselected = []
    bstack1lll1lllllll_opy_ = set()
    for selector in bstack1lll1llll11l_opy_:
        if not selector or not isinstance(selector, str):
            continue
        bstack1lll1lllllll_opy_.add(selector)
    for item in items:
        nodeid = getattr(item, bstack11ll_opy_ (u"ࠫࡳࡵࡤࡦ࡫ࡧࠫⓙ"), None)
        if not nodeid:
            deselected.append(item)
            continue
        if (
            nodeid in bstack1lll1lllllll_opy_ or
            any(sel in nodeid for sel in bstack1lll1lllllll_opy_)
        ):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
@bstack1l111l1l_opy_.bstack1llll11l11ll_opy_
def bstack1lll1ll11l1l_opy_():
    bstack1lll1ll1l111_opy_()
    if cli.is_running():
        try:
            bstack11l1l1l1l1l_opy_(bstack1llll111111l_opy_)
        except Exception as e:
            logger.debug(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࡵࠣࡴࡦࡺࡣࡩ࠼ࠣࡿࢂࠨⓚ").format(e))
        return
    if bstack11llll1l1l_opy_():
        bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
        bstack11ll_opy_ (u"࠭ࠧࠨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡵࡶࡰࠡ࠿ࠣ࠵࠱ࠦ࡭ࡰࡦࡢࡩࡽ࡫ࡣࡶࡶࡨࠤ࡬࡫ࡴࡴࠢࡸࡷࡪࡪࠠࡧࡱࡵࠤࡦ࠷࠱ࡺࠢࡦࡳࡲࡳࡡ࡯ࡦࡶ࠱ࡼࡸࡡࡱࡲ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡲࡳࡴࠥࡄࠠ࠲࠮ࠣࡱࡴࡪ࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡣࡧࡦࡥࡺࡹࡥࠡ࡫ࡷࠤ࡮ࡹࠠࡱࡣࡷࡧ࡭࡫ࡤࠡ࡫ࡱࠤࡦࠦࡤࡪࡨࡩࡩࡷ࡫࡮ࡵࠢࡳࡶࡴࡩࡥࡴࡵࠣ࡭ࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡵࡴࠢࡺࡩࠥࡴࡥࡦࡦࠣࡸࡴࠦࡵࡴࡧࠣࡗࡪࡲࡥ࡯࡫ࡸࡱࡕࡧࡴࡤࡪࠫࡷࡪࡲࡥ࡯࡫ࡸࡱࡤ࡮ࡡ࡯ࡦ࡯ࡩࡷ࠯ࠠࡧࡱࡵࠤࡵࡶࡰࠡࡀࠣ࠵ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧࠨࠩⓛ")
        if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫⓜ")):
            if CONFIG.get(bstack11ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨⓝ")) is not None and int(CONFIG[bstack11ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩⓞ")]) > 1:
                bstack11l111ll11_opy_(bstack11llllll11_opy_)
            return
        bstack11l111ll11_opy_(bstack11llllll11_opy_)
    try:
        bstack11l1l1l1l1l_opy_(bstack1llll111111l_opy_)
    except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࡳࠡࡲࡤࡸࡨ࡮࠺ࠡࡽࢀࠦⓟ").format(e))
bstack1lll1ll11l1l_opy_()