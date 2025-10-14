# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1l1l1111ll_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111ll1ll11_opy_, bstack1ll1ll1111_opy_, update, bstack11ll111l1l_opy_,
                                       bstack1l11lll11l_opy_, bstack1l1111111_opy_, bstack1l111l111l_opy_, bstack11lll11l1_opy_,
                                       bstack1l1l11ll1l_opy_, bstack1l111lll11_opy_, bstack11111l1ll1_opy_,
                                       bstack11l1111ll1_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack111ll1lll1_opy_)
from browserstack_sdk.bstack111llll1_opy_ import bstack11111l11_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1ll1111ll_opy_
from bstack_utils.capture import bstack1l11l111_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack1l11lllll1_opy_, bstack1ll1l1l111_opy_, bstack11111l111_opy_, \
    bstack1ll1ll1ll1_opy_
from bstack_utils.helper import bstack11lll111_opy_, bstack111l1l11lll_opy_, bstack1ll1l111_opy_, bstack11111lll1_opy_, bstack1llll11llll_opy_, bstack1ll1ll11_opy_, \
    bstack1111lllllll_opy_, \
    bstack111l1lllll1_opy_, bstack11lll11ll_opy_, bstack1ll111l1l1_opy_, bstack111l11lll11_opy_, bstack11ll1ll11_opy_, Notset, \
    bstack11ll1lllll_opy_, bstack1111l1ll11l_opy_, bstack111l11l11ll_opy_, Result, bstack111l1lll1ll_opy_, bstack111l1ll1lll_opy_, error_handler, \
    bstack11l1ll111_opy_, bstack1ll111ll1l_opy_, bstack1lll1ll1l1_opy_, bstack111l1l11ll1_opy_
from bstack_utils.bstack11l1ll1111l_opy_ import bstack11l1l1lllll_opy_
from bstack_utils.messages import bstack111lllll1l_opy_, bstack11111ll111_opy_, bstack11l1111111_opy_, bstack11l1l1111_opy_, bstack111l11ll_opy_, \
    bstack1l1llll1ll_opy_, bstack1l11ll1ll1_opy_, bstack1ll1lll1l1_opy_, bstack11l1l1lll_opy_, bstack1ll1l1ll1_opy_, \
    bstack1l1ll1lll1_opy_, bstack1lll1l1l1l_opy_, bstack1l1ll11lll_opy_
from bstack_utils.proxy import bstack1l111ll1l_opy_, bstack1l1ll111ll_opy_
from bstack_utils.bstack1ll111lll_opy_ import bstack11l111llll1_opy_, bstack11l11l11l11_opy_, bstack11l111lll11_opy_, bstack11l111ll1ll_opy_, \
    bstack11l11l1111l_opy_, bstack11l11l111l1_opy_, bstack11l111lllll_opy_, bstack1lll11ll11_opy_, bstack11l11l11111_opy_
from bstack_utils.bstack1lll111lll_opy_ import bstack1l1lll1ll_opy_
from bstack_utils.bstack1111l1l11_opy_ import bstack1lll1ll11l_opy_, bstack11llll1ll1_opy_, bstack11l1llllll_opy_, \
    bstack11ll1111ll_opy_, bstack1ll1lllll_opy_
from bstack_utils.bstack1l11lll1_opy_ import bstack11lllll1_opy_
from bstack_utils.bstack11llllll_opy_ import bstack1ll1l1ll_opy_
import bstack_utils.accessibility as bstack111l1lll_opy_
from bstack_utils.bstack1l11l1ll_opy_ import bstack1l1lll1l_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack11l1ll11ll_opy_
from bstack_utils.bstack1llll11l1_opy_ import bstack11l1l111_opy_
from browserstack_sdk.__init__ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1l11llll111_opy_ import bstack1l1l11l11ll_opy_
from browserstack_sdk.sdk_cli.bstack11l11lllll_opy_ import bstack11l11lllll_opy_, Events, bstack111llll1ll_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1ll1l1lll11_opy_, bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11l11lllll_opy_ import bstack11l11lllll_opy_, Events, bstack111llll1ll_opy_
bstack111ll11l11_opy_ = None
bstack1111llll1l_opy_ = None
bstack11111l1l1_opy_ = None
bstack1lll11l111_opy_ = None
bstack11l11llll1_opy_ = None
bstack1l1111l1l_opy_ = None
bstack1lllll11l1_opy_ = None
bstack11111ll1l_opy_ = None
bstack1ll1lll111_opy_ = None
bstack11l111l111_opy_ = None
bstack11ll11l1l1_opy_ = None
bstack1llllll1ll_opy_ = None
bstack111ll1111_opy_ = None
bstack11l11l1ll_opy_ = bstack11l1l11_opy_ (u"ࠪࠫ≍")
CONFIG = {}
bstack11l1l1111l_opy_ = False
bstack1ll1l11l1l_opy_ = bstack11l1l11_opy_ (u"ࠫࠬ≎")
bstack111ll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭≏")
bstack11ll1ll1l1_opy_ = False
bstack11llll1l11_opy_ = []
bstack1l1l111lll_opy_ = bstack1l11lllll1_opy_
bstack1lll1lll1l1l_opy_ = bstack11l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭≐")
bstack1llll111l1_opy_ = {}
bstack1111ll11l_opy_ = None
bstack11l1ll1lll_opy_ = False
logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1l1l111lll_opy_)
store = {
    bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ≑"): []
}
bstack1llll111111l_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l1l11ll_opy_ = {}
current_test_uuid = None
cli_context = bstack1ll1l1lll11_opy_(
    test_framework_name=bstack11ll1l11ll_opy_[bstack11l1l11_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈࠬ≒")] if bstack11ll1ll11_opy_() else bstack11ll1l11ll_opy_[bstack11l1l11_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩ≓")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1111l1ll1l_opy_(page, bstack1ll1ll111l_opy_):
    try:
        page.evaluate(bstack11l1l11_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ≔"),
                      bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ≕") + json.dumps(
                          bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠧࢃࡽࠣ≖"))
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦ≗"), e)
def bstack1lll1lllll_opy_(page, message, level):
    try:
        page.evaluate(bstack11l1l11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ≘"), bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭≙") + json.dumps(
            message) + bstack11l1l11_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬ≚") + json.dumps(level) + bstack11l1l11_opy_ (u"ࠪࢁࢂ࠭≛"))
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢ≜"), e)
def pytest_configure(config):
    global bstack1ll1l11l1l_opy_
    global CONFIG
    bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
    config.args = bstack1ll1l1ll_opy_.bstack11l11l1l11l_opy_(config.args)
    bstack111111ll_opy_.bstack1l111l1111_opy_(bstack1lll1ll1l1_opy_(config.getoption(bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ≝"))))
    try:
        bstack1ll1111ll_opy_.bstack1111l11111l_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack11l11lllll_opy_.invoke(Events.CONNECT, bstack111llll1ll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭≞"), bstack11l1l11_opy_ (u"ࠧ࠱ࠩ≟")))
        config = json.loads(os.environ.get(bstack11l1l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢ≠"), bstack11l1l11_opy_ (u"ࠤࡾࢁࠧ≡")))
        cli.bstack1l1l1ll1l11_opy_(bstack1ll111l1l1_opy_(bstack1ll1l11l1l_opy_, CONFIG), cli_context.platform_index, bstack11ll111l1l_opy_)
    if cli.bstack1l1ll11l1ll_opy_(bstack1l1l11l11ll_opy_):
        cli.bstack1l11lllllll_opy_()
        logger.debug(bstack11l1l11_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤ≢") + str(cli_context.platform_index) + bstack11l1l11_opy_ (u"ࠦࠧ≣"))
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.BEFORE_ALL, bstack1llll1111l1_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11l1l11_opy_ (u"ࠧࡽࡨࡦࡰࠥ≤"), None)
    if cli.is_running() and when == bstack11l1l11_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ≥"):
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.LOG_REPORT, bstack1llll1111l1_opy_.PRE, item, call)
    outcome = yield
    if when == bstack11l1l11_opy_ (u"ࠢࡤࡣ࡯ࡰࠧ≦"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1l11_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ≧")))
        if not passed:
            config = json.loads(os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠣ≨"), bstack11l1l11_opy_ (u"ࠥࡿࢂࠨ≩")))
            if bstack11l1l111_opy_.bstack1lll1l1ll_opy_(config):
                bstack111111l1ll1_opy_ = bstack11l1l111_opy_.bstack1lllll111_opy_(config)
                if item.execution_count > bstack111111l1ll1_opy_:
                    print(bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡴࡨࡸࡷ࡯ࡥࡴ࠼ࠣࠫ≪"), report.nodeid, os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ≫")))
                    bstack11l1l111_opy_.bstack111lll1ll1l_opy_(report.nodeid)
            else:
                print(bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥ࠭≬"), report.nodeid, os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ≭")))
                bstack11l1l111_opy_.bstack111lll1ll1l_opy_(report.nodeid)
        else:
            print(bstack11l1l11_opy_ (u"ࠨࡖࡨࡷࡹࠦࡰࡢࡵࡶࡩࡩࡀࠠࠨ≮"), report.nodeid, os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ≯")))
    if cli.is_running():
        if when == bstack11l1l11_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ≰"):
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.BEFORE_EACH, bstack1llll1111l1_opy_.POST, item, call, outcome)
        elif when == bstack11l1l11_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ≱"):
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.LOG_REPORT, bstack1llll1111l1_opy_.POST, item, call, outcome)
        elif when == bstack11l1l11_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ≲"):
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.AFTER_EACH, bstack1llll1111l1_opy_.POST, item, call, outcome)
        return # skip all existing operations
    skipSessionName = item.config.getoption(bstack11l1l11_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ≳"))
    plugins = item.config.getoption(bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡸ࡫࡮ࡴࡳࠣ≴"))
    report = outcome.get_result()
    os.environ[bstack11l1l11_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ≵")] = report.nodeid
    bstack1llll1111l1l_opy_(item, call, report)
    if bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠢ≶") not in plugins or bstack11ll1ll11_opy_():
        return
    summary = []
    driver = getattr(item, bstack11l1l11_opy_ (u"ࠥࡣࡩࡸࡩࡷࡧࡵࠦ≷"), None)
    page = getattr(item, bstack11l1l11_opy_ (u"ࠦࡤࡶࡡࡨࡧࠥ≸"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1llll1111111_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1lll1lll1111_opy_(item, report, summary, skipSessionName)
def bstack1llll1111111_opy_(item, report, summary, skipSessionName):
    if report.when == bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ≹") and report.skipped:
        bstack11l11l11111_opy_(report)
    if report.when in [bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧ≺"), bstack11l1l11_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ≻")]:
        return
    if not bstack1llll11llll_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack11l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭≼")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ≽") + json.dumps(
                    report.nodeid) + bstack11l1l11_opy_ (u"ࠪࢁࢂ࠭≾"))
        os.environ[bstack11l1l11_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧ≿")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11l1l11_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫࠺ࠡࡽ࠳ࢁࠧ⊀").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1l11_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ⊁")))
    bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠢࠣ⊂")
    bstack11l11l11111_opy_(report)
    if not passed:
        try:
            bstack1ll1llll11_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11l1l11_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣ⊃").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1llll11_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11l1l11_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ⊄")))
        bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠥࠦ⊅")
        if not passed:
            try:
                bstack1ll1llll11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1l11_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦ⊆").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1ll1llll11_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩ⊇")
                    + json.dumps(bstack11l1l11_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠧࠢ⊈"))
                    + bstack11l1l11_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥ⊉")
                )
            else:
                item._driver.execute_script(
                    bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡪࡡࡵࡣࠥ࠾ࠥ࠭⊊")
                    + json.dumps(str(bstack1ll1llll11_opy_))
                    + bstack11l1l11_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧ⊋")
                )
        except Exception as e:
            summary.append(bstack11l1l11_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡣࡱࡲࡴࡺࡡࡵࡧ࠽ࠤࢀ࠶ࡽࠣ⊌").format(e))
def bstack1llll1111ll1_opy_(test_name, error_message):
    try:
        bstack1lll1llllll1_opy_ = []
        bstack11111l11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⊍"), bstack11l1l11_opy_ (u"ࠬ࠶ࠧ⊎"))
        bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⊏"): test_name, bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⊐"): error_message, bstack11l1l11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ⊑"): bstack11111l11l_opy_}
        bstack1llll111l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ⊒"))
        if os.path.exists(bstack1llll111l1l1_opy_):
            with open(bstack1llll111l1l1_opy_) as f:
                bstack1lll1llllll1_opy_ = json.load(f)
        bstack1lll1llllll1_opy_.append(bstack11ll11ll1_opy_)
        with open(bstack1llll111l1l1_opy_, bstack11l1l11_opy_ (u"ࠪࡻࠬ⊓")) as f:
            json.dump(bstack1lll1llllll1_opy_, f)
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡦࡴࡶ࡭ࡸࡺࡩ࡯ࡩࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡱࡻࡷࡩࡸࡺࠠࡦࡴࡵࡳࡷࡹ࠺ࠡࠩ⊔") + str(e))
def bstack1lll1lll1111_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack11l1l11_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ⊕"), bstack11l1l11_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣ⊖")]:
        return
    if (str(skipSessionName).lower() != bstack11l1l11_opy_ (u"ࠧࡵࡴࡸࡩࠬ⊗")):
        bstack1111l1ll1l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11l1l11_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ⊘")))
    bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠤࠥ⊙")
    bstack11l11l11111_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1ll1llll11_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11l1l11_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ⊚").format(e)
                )
        try:
            if passed:
                bstack1ll1lllll_opy_(getattr(item, bstack11l1l11_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪ⊛"), None), bstack11l1l11_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ⊜"))
            else:
                error_message = bstack11l1l11_opy_ (u"࠭ࠧ⊝")
                if bstack1ll1llll11_opy_:
                    bstack1lll1lllll_opy_(item._page, str(bstack1ll1llll11_opy_), bstack11l1l11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ⊞"))
                    bstack1ll1lllll_opy_(getattr(item, bstack11l1l11_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧ⊟"), None), bstack11l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ⊠"), str(bstack1ll1llll11_opy_))
                    error_message = str(bstack1ll1llll11_opy_)
                else:
                    bstack1ll1lllll_opy_(getattr(item, bstack11l1l11_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩ⊡"), None), bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ⊢"))
                bstack1llll1111ll1_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11l1l11_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁ࠰ࡾࠤ⊣").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11l1l11_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ⊤"), default=bstack11l1l11_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨ⊥"), help=bstack11l1l11_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢ⊦"))
    parser.addoption(bstack11l1l11_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ⊧"), default=bstack11l1l11_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤ⊨"), help=bstack11l1l11_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥ⊩"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11l1l11_opy_ (u"ࠧ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠢ⊪"), action=bstack11l1l11_opy_ (u"ࠨࡳࡵࡱࡵࡩࠧ⊫"), default=bstack11l1l11_opy_ (u"ࠢࡤࡪࡵࡳࡲ࡫ࠢ⊬"),
                         help=bstack11l1l11_opy_ (u"ࠣࡆࡵ࡭ࡻ࡫ࡲࠡࡶࡲࠤࡷࡻ࡮ࠡࡶࡨࡷࡹࡹࠢ⊭"))
def bstack1l1ll1ll_opy_(log):
    if not (log[bstack11l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⊮")] and log[bstack11l1l11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⊯")].strip()):
        return
    active = bstack1ll11l11_opy_()
    log = {
        bstack11l1l11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⊰"): log[bstack11l1l11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⊱")],
        bstack11l1l11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⊲"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"࡛ࠧࠩ⊳"),
        bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⊴"): log[bstack11l1l11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⊵")],
    }
    if active:
        if active[bstack11l1l11_opy_ (u"ࠪࡸࡾࡶࡥࠨ⊶")] == bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⊷"):
            log[bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⊸")] = active[bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⊹")]
        elif active[bstack11l1l11_opy_ (u"ࠧࡵࡻࡳࡩࠬ⊺")] == bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹ࠭⊻"):
            log[bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⊼")] = active[bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⊽")]
    bstack1l1lll1l_opy_.bstack1l1l1111_opy_([log])
def bstack1ll11l11_opy_():
    if len(store[bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ⊾")]) > 0 and store[bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⊿")][-1]:
        return {
            bstack11l1l11_opy_ (u"࠭ࡴࡺࡲࡨࠫ⋀"): bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ⋁"),
            bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⋂"): store[bstack11l1l11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⋃")][-1]
        }
    if store.get(bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⋄"), None):
        return {
            bstack11l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩ⋅"): bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࠪ⋆"),
            bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⋇"): store[bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⋈")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.INIT_TEST, bstack1llll1111l1_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.INIT_TEST, bstack1llll1111l1_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1lll1llll1ll_opy_ = True
        bstack1lll111111_opy_ = bstack111l1lll_opy_.bstack111111l1l_opy_(bstack111l1lllll1_opy_(item.own_markers))
        if not cli.bstack1l1ll11l1ll_opy_(bstack1l1l11l11ll_opy_):
            item._a11y_test_case = bstack1lll111111_opy_
            if bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ⋉"), None):
                driver = getattr(item, bstack11l1l11_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⋊"), None)
                item._a11y_started = bstack111l1lll_opy_.bstack11l111111_opy_(driver, bstack1lll111111_opy_)
        if not bstack1l1lll1l_opy_.on() or bstack1lll1lll1l1l_opy_ != bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ⋋"):
            return
        global current_test_uuid #, bstack1l11111l_opy_
        bstack1l11l11l_opy_ = {
            bstack11l1l11_opy_ (u"ࠫࡺࡻࡩࡥࠩ⋌"): uuid4().__str__(),
            bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⋍"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"࡚࠭ࠨ⋎")
        }
        current_test_uuid = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⋏")]
        store[bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⋐")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⋑")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l1l11ll_opy_[item.nodeid] = {**_1l1l11ll_opy_[item.nodeid], **bstack1l11l11l_opy_}
        bstack1llll111l1ll_opy_(item, _1l1l11ll_opy_[item.nodeid], bstack11l1l11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⋒"))
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡨࡧ࡬࡭࠼ࠣࡿࢂ࠭⋓"), str(err))
def pytest_runtest_setup(item):
    store[bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⋔")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.BEFORE_EACH, bstack1llll1111l1_opy_.PRE, item, bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⋕"))
    if bstack11l1l111_opy_.bstack11l111ll11l_opy_():
            bstack1lll1ll1llll_opy_ = bstack11l1l11_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡢࡵࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦ⋖")
            logger.error(bstack1lll1ll1llll_opy_)
            bstack1l11l11l_opy_ = {
                bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⋗"): uuid4().__str__(),
                bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⋘"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"ࠪ࡞ࠬ⋙"),
                bstack11l1l11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⋚"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"ࠬࡠࠧ⋛"),
                bstack11l1l11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⋜"): bstack11l1l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⋝"),
                bstack11l1l11_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ⋞"): bstack1lll1ll1llll_opy_,
                bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⋟"): [],
                bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ⋠"): []
            }
            bstack1llll111l1ll_opy_(item, bstack1l11l11l_opy_, bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⋡"))
            pytest.skip(bstack1lll1ll1llll_opy_)
            return # skip all existing operations
    global bstack1llll111111l_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l11lll11_opy_():
        atexit.register(bstack111l1l1l1l_opy_)
        if not bstack1llll111111l_opy_:
            try:
                bstack1lll1lll111l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111l1l11ll1_opy_():
                    bstack1lll1lll111l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll1lll111l_opy_:
                    signal.signal(s, bstack1llll1111l11_opy_)
                bstack1llll111111l_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡪ࡭ࡸࡺࡥࡳࠢࡶ࡭࡬ࡴࡡ࡭ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࡶ࠾ࠥࠨ⋢") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l111llll1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11l1l11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⋣")
    try:
        if not bstack1l1lll1l_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1l11l11l_opy_ = {
            bstack11l1l11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⋤"): uuid,
            bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⋥"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"ࠩ࡝ࠫ⋦"),
            bstack11l1l11_opy_ (u"ࠪࡸࡾࡶࡥࠨ⋧"): bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩ⋨"),
            bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⋩"): bstack11l1l11_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ⋪"),
            bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ⋫"): bstack11l1l11_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⋬")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11l1l11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭⋭")] = item
        store[bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⋮")] = [uuid]
        if not _1l1l11ll_opy_.get(item.nodeid, None):
            _1l1l11ll_opy_[item.nodeid] = {bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⋯"): [], bstack11l1l11_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⋰"): []}
        _1l1l11ll_opy_[item.nodeid][bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⋱")].append(bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⋲")])
        _1l1l11ll_opy_[item.nodeid + bstack11l1l11_opy_ (u"ࠨ࠯ࡶࡩࡹࡻࡰࠨ⋳")] = bstack1l11l11l_opy_
        bstack1lll1lllllll_opy_(item, bstack1l11l11l_opy_, bstack11l1l11_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⋴"))
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡷࡪࡺࡵࡱ࠼ࠣࡿࢂ࠭⋵"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.AFTER_EACH, bstack1llll1111l1_opy_.PRE, item, bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⋶"))
        return # skip all existing operations
    try:
        global bstack1llll111l1_opy_
        bstack11111l11l_opy_ = 0
        if bstack11ll1ll1l1_opy_ is True:
            bstack11111l11l_opy_ = int(os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ⋷")))
        if bstack11ll1lll1l_opy_.bstack1llll11111_opy_() == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦ⋸"):
            if bstack11ll1lll1l_opy_.bstack11l1lllll1_opy_() == bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ⋹"):
                bstack1lll1lll1l11_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⋺"), None)
                bstack1lllll111l_opy_ = bstack1lll1lll1l11_opy_ + bstack11l1l11_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧ⋻")
                driver = getattr(item, bstack11l1l11_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ⋼"), None)
                bstack111ll1l11l_opy_ = getattr(item, bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⋽"), None)
                bstack11llll1l1_opy_ = getattr(item, bstack11l1l11_opy_ (u"ࠬࡻࡵࡪࡦࠪ⋾"), None)
                PercySDK.screenshot(driver, bstack1lllll111l_opy_, bstack111ll1l11l_opy_=bstack111ll1l11l_opy_, bstack11llll1l1_opy_=bstack11llll1l1_opy_, bstack1l1l1llll1_opy_=bstack11111l11l_opy_)
        if not cli.bstack1l1ll11l1ll_opy_(bstack1l1l11l11ll_opy_):
            if getattr(item, bstack11l1l11_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡢࡴࡷࡩࡩ࠭⋿"), False):
                bstack11111l11_opy_.bstack11111ll1_opy_(getattr(item, bstack11l1l11_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⌀"), None), bstack1llll111l1_opy_, logger, item)
        if not bstack1l1lll1l_opy_.on():
            return
        bstack1l11l11l_opy_ = {
            bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⌁"): uuid4().__str__(),
            bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⌂"): bstack1ll1l111_opy_().isoformat() + bstack11l1l11_opy_ (u"ࠪ࡞ࠬ⌃"),
            bstack11l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩ⌄"): bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⌅"),
            bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⌆"): bstack11l1l11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ⌇"),
            bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ⌈"): bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ⌉")
        }
        _1l1l11ll_opy_[item.nodeid + bstack11l1l11_opy_ (u"ࠪ࠱ࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭⌊")] = bstack1l11l11l_opy_
        bstack1lll1lllllll_opy_(item, bstack1l11l11l_opy_, bstack11l1l11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⌋"))
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࠺ࠡࡽࢀࠫ⌌"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111ll1ll_opy_(fixturedef.argname):
        store[bstack11l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬ⌍")] = request.node
    elif bstack11l11l1111l_opy_(fixturedef.argname):
        store[bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬ⌎")] = request.node
    if not bstack1l1lll1l_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.SETUP_FIXTURE, bstack1llll1111l1_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.SETUP_FIXTURE, bstack1llll1111l1_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.SETUP_FIXTURE, bstack1llll1111l1_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.SETUP_FIXTURE, bstack1llll1111l1_opy_.POST, fixturedef, request, outcome)
        return # skip all existing operations
    try:
        fixture = {
            bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭⌏"): fixturedef.argname,
            bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⌐"): bstack1111lllllll_opy_(outcome),
            bstack11l1l11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⌑"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ⌒")]
        if not _1l1l11ll_opy_.get(current_test_item.nodeid, None):
            _1l1l11ll_opy_[current_test_item.nodeid] = {bstack11l1l11_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧ⌓"): []}
        _1l1l11ll_opy_[current_test_item.nodeid][bstack11l1l11_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⌔")].append(fixture)
    except Exception as err:
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡴࡧࡷࡹࡵࡀࠠࡼࡿࠪ⌕"), str(err))
if bstack11ll1ll11_opy_() and bstack1l1lll1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.STEP, bstack1llll1111l1_opy_.PRE, request, step)
            return
        try:
            _1l1l11ll_opy_[request.node.nodeid][bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ⌖")].bstack11ll11l1_opy_(id(step))
        except Exception as err:
            print(bstack11l1l11_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲ࠽ࠤࢀࢃࠧ⌗"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.STEP, bstack1llll1111l1_opy_.POST, request, step, exception)
            return
        try:
            _1l1l11ll_opy_[request.node.nodeid][bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⌘")].bstack1lll11ll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11l1l11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ⌙"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.STEP, bstack1llll1111l1_opy_.POST, request, step)
            return
        try:
            bstack1l11lll1_opy_: bstack11lllll1_opy_ = _1l1l11ll_opy_[request.node.nodeid][bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⌚")]
            bstack1l11lll1_opy_.bstack1lll11ll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11l1l11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪ⌛"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1lll1l1l_opy_
        try:
            if not bstack1l1lll1l_opy_.on() or bstack1lll1lll1l1l_opy_ != bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⌜"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.PRE, request, feature, scenario)
                return
            driver = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ⌝"), None)
            if not _1l1l11ll_opy_.get(request.node.nodeid, None):
                _1l1l11ll_opy_[request.node.nodeid] = {}
            bstack1l11lll1_opy_ = bstack11lllll1_opy_.bstack11111l11111_opy_(
                scenario, feature, request.node,
                name=bstack11l11l111l1_opy_(request.node, scenario),
                started_at=bstack1ll1ll11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11l1l11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ⌞"),
                tags=bstack11l111lllll_opy_(feature, scenario),
                bstack1l111ll1_opy_=bstack1l1lll1l_opy_.bstack1ll1l1l1_opy_(driver) if driver and driver.session_id else {}
            )
            _1l1l11ll_opy_[request.node.nodeid][bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭⌟")] = bstack1l11lll1_opy_
            bstack1lll1lll1lll_opy_(bstack1l11lll1_opy_.uuid)
            bstack1l1lll1l_opy_.bstack1llll111_opy_(bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⌠"), bstack1l11lll1_opy_)
        except Exception as err:
            print(bstack11l1l11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧ⌡"), str(err))
def bstack1lll1lllll1l_opy_(bstack11l1ll1l_opy_):
    if bstack11l1ll1l_opy_ in store[bstack11l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ⌢")]:
        store[bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⌣")].remove(bstack11l1ll1l_opy_)
def bstack1lll1lll1lll_opy_(test_uuid):
    store[bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⌤")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1l1lll1l_opy_.bstack1llll1l1ll11_opy_
def bstack1llll1111l1l_opy_(item, call, report):
    logger.debug(bstack11l1l11_opy_ (u"ࠩ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡹࡴࡢࡴࡷࠫ⌥"))
    global bstack1lll1lll1l1l_opy_
    bstack1l11ll1l1l_opy_ = bstack1ll1ll11_opy_()
    if hasattr(report, bstack11l1l11_opy_ (u"ࠪࡷࡹࡵࡰࠨ⌦")):
        bstack1l11ll1l1l_opy_ = bstack111l1lll1ll_opy_(report.stop)
    elif hasattr(report, bstack11l1l11_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪ⌧")):
        bstack1l11ll1l1l_opy_ = bstack111l1lll1ll_opy_(report.start)
    try:
        if getattr(report, bstack11l1l11_opy_ (u"ࠬࡽࡨࡦࡰࠪ⌨"), bstack11l1l11_opy_ (u"࠭ࠧ〈")) == bstack11l1l11_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ〉"):
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡪࡤࡲࡩࡲࡥࡠࡱ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡸࡺࡡࡵࡧࠣ࠱ࠥࢁࡽ࠭ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥ࠳ࠠࡼࡿࠪ⌫").format(getattr(report, bstack11l1l11_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ⌬"), bstack11l1l11_opy_ (u"ࠪࠫ⌭")).__str__(), bstack1lll1lll1l1l_opy_))
            if bstack1lll1lll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⌮"):
                _1l1l11ll_opy_[item.nodeid][bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⌯")] = bstack1l11ll1l1l_opy_
                bstack1llll111l1ll_opy_(item, _1l1l11ll_opy_[item.nodeid], bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⌰"), report, call)
                store[bstack11l1l11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⌱")] = None
            elif bstack1lll1lll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ⌲"):
                bstack1l11lll1_opy_ = _1l1l11ll_opy_[item.nodeid][bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⌳")]
                bstack1l11lll1_opy_.set(hooks=_1l1l11ll_opy_[item.nodeid].get(bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⌴"), []))
                exception, bstack11lll1l1_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll1l1_opy_ = [call.excinfo.exconly(), getattr(report, bstack11l1l11_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪ⌵"), bstack11l1l11_opy_ (u"ࠬ࠭⌶"))]
                bstack1l11lll1_opy_.stop(time=bstack1l11ll1l1l_opy_, result=Result(result=getattr(report, bstack11l1l11_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ⌷"), bstack11l1l11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⌸")), exception=exception, bstack11lll1l1_opy_=bstack11lll1l1_opy_))
                bstack1l1lll1l_opy_.bstack1llll111_opy_(bstack11l1l11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⌹"), _1l1l11ll_opy_[item.nodeid][bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ⌺")])
        elif getattr(report, bstack11l1l11_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ⌻"), bstack11l1l11_opy_ (u"ࠫࠬ⌼")) in [bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ⌽"), bstack11l1l11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ⌾")]:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡴࡦࠢ࠰ࠤࢀࢃࠬࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࠲ࠦࡻࡾࠩ⌿").format(getattr(report, bstack11l1l11_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⍀"), bstack11l1l11_opy_ (u"ࠩࠪ⍁")).__str__(), bstack1lll1lll1l1l_opy_))
            bstack1l111111_opy_ = item.nodeid + bstack11l1l11_opy_ (u"ࠪ࠱ࠬ⍂") + getattr(report, bstack11l1l11_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍃"), bstack11l1l11_opy_ (u"ࠬ࠭⍄"))
            if getattr(report, bstack11l1l11_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ⍅"), False):
                hook_type = bstack11l1l11_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ⍆") if getattr(report, bstack11l1l11_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭⍇"), bstack11l1l11_opy_ (u"ࠩࠪ⍈")) == bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⍉") else bstack11l1l11_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨ⍊")
                _1l1l11ll_opy_[bstack1l111111_opy_] = {
                    bstack11l1l11_opy_ (u"ࠬࡻࡵࡪࡦࠪ⍋"): uuid4().__str__(),
                    bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⍌"): bstack1l11ll1l1l_opy_,
                    bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⍍"): hook_type
                }
            _1l1l11ll_opy_[bstack1l111111_opy_][bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⍎")] = bstack1l11ll1l1l_opy_
            bstack1lll1lllll1l_opy_(_1l1l11ll_opy_[bstack1l111111_opy_][bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⍏")])
            bstack1lll1lllllll_opy_(item, _1l1l11ll_opy_[bstack1l111111_opy_], bstack11l1l11_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⍐"), report, call)
            if getattr(report, bstack11l1l11_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩ⍑"), bstack11l1l11_opy_ (u"ࠬ࠭⍒")) == bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ⍓"):
                if getattr(report, bstack11l1l11_opy_ (u"ࠧࡰࡷࡷࡧࡴࡳࡥࠨ⍔"), bstack11l1l11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ⍕")) == bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⍖"):
                    bstack1l11l11l_opy_ = {
                        bstack11l1l11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍗"): uuid4().__str__(),
                        bstack11l1l11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⍘"): bstack1ll1ll11_opy_(),
                        bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⍙"): bstack1ll1ll11_opy_()
                    }
                    _1l1l11ll_opy_[item.nodeid] = {**_1l1l11ll_opy_[item.nodeid], **bstack1l11l11l_opy_}
                    bstack1llll111l1ll_opy_(item, _1l1l11ll_opy_[item.nodeid], bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⍚"))
                    bstack1llll111l1ll_opy_(item, _1l1l11ll_opy_[item.nodeid], bstack11l1l11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⍛"), report, call)
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡿࢂ࠭⍜"), str(err))
def bstack1lll1lllll11_opy_(test, bstack1l11l11l_opy_, result=None, call=None, bstack11111111l_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l11lll1_opy_ = {
        bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⍝"): bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⍞")],
        bstack11l1l11_opy_ (u"ࠫࡹࡿࡰࡦࠩ⍟"): bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࠪ⍠"),
        bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⍡"): test.name,
        bstack11l1l11_opy_ (u"ࠧࡣࡱࡧࡽࠬ⍢"): {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭⍣"): bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ⍤"),
            bstack11l1l11_opy_ (u"ࠪࡧࡴࡪࡥࠨ⍥"): inspect.getsource(test.obj)
        },
        bstack11l1l11_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ⍦"): test.name,
        bstack11l1l11_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫ⍧"): test.name,
        bstack11l1l11_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭⍨"): bstack1ll1l1ll_opy_.bstack1l1l1l1l_opy_(test),
        bstack11l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ⍩"): file_path,
        bstack11l1l11_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪ⍪"): file_path,
        bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⍫"): bstack11l1l11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⍬"),
        bstack11l1l11_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩ⍭"): file_path,
        bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⍮"): bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⍯")],
        bstack11l1l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ⍰"): bstack11l1l11_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ⍱"),
        bstack11l1l11_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬ⍲"): {
            bstack11l1l11_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧ⍳"): test.nodeid
        },
        bstack11l1l11_opy_ (u"ࠫࡹࡧࡧࡴࠩ⍴"): bstack111l1lllll1_opy_(test.own_markers)
    }
    if bstack11111111l_opy_ in [bstack11l1l11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭⍵"), bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⍶")]:
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠧ࡮ࡧࡷࡥࠬ⍷")] = {
            bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ⍸"): bstack1l11l11l_opy_.get(bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫ⍹"), [])
        }
    if bstack11111111l_opy_ == bstack11l1l11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫ⍺"):
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⍻")] = bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⍼")
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⍽")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⍾")]
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⍿")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⎀")]
    if result:
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⎁")] = result.outcome
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⎂")] = result.duration * 1000
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎃")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎄")]
        if result.failed:
            bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⎅")] = bstack1l1lll1l_opy_.bstack11111l111l_opy_(call.excinfo.typename)
            bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩ⎆")] = bstack1l1lll1l_opy_.bstack1llll11ll1ll_opy_(call.excinfo, result)
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎇")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⎈")]
    if outcome:
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⎉")] = bstack1111lllllll_opy_(outcome)
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭⎊")] = 0
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⎋")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⎌")]
        if bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⎍")] == bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⎎"):
            bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩ⎏")] = bstack11l1l11_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬ⎐")  # bstack1lll1ll1ll11_opy_
            bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⎑")] = [{bstack11l1l11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⎒"): [bstack11l1l11_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫ⎓")]}]
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⎔")] = bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ⎕")]
    return bstack1l11lll1_opy_
def bstack1llll11111ll_opy_(test, bstack1lll111l_opy_, bstack11111111l_opy_, result, call, outcome, bstack1llll11111l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭⎖")]
    hook_name = bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ⎗")]
    hook_data = {
        bstack11l1l11_opy_ (u"ࠬࡻࡵࡪࡦࠪ⎘"): bstack1lll111l_opy_[bstack11l1l11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⎙")],
        bstack11l1l11_opy_ (u"ࠧࡵࡻࡳࡩࠬ⎚"): bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰ࠭⎛"),
        bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ⎜"): bstack11l1l11_opy_ (u"ࠪࡿࢂ࠭⎝").format(bstack11l11l11l11_opy_(hook_name)),
        bstack11l1l11_opy_ (u"ࠫࡧࡵࡤࡺࠩ⎞"): {
            bstack11l1l11_opy_ (u"ࠬࡲࡡ࡯ࡩࠪ⎟"): bstack11l1l11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭⎠"),
            bstack11l1l11_opy_ (u"ࠧࡤࡱࡧࡩࠬ⎡"): None
        },
        bstack11l1l11_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧ⎢"): test.name,
        bstack11l1l11_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩ⎣"): bstack1ll1l1ll_opy_.bstack1l1l1l1l_opy_(test, hook_name),
        bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭⎤"): file_path,
        bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭⎥"): file_path,
        bstack11l1l11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎦"): bstack11l1l11_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⎧"),
        bstack11l1l11_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬ⎨"): file_path,
        bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ⎩"): bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭⎪")],
        bstack11l1l11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭⎫"): bstack11l1l11_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭⎬") if bstack1lll1lll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ⎭") else bstack11l1l11_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭⎮"),
        bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⎯"): hook_type
    }
    bstack1l111ll1lll_opy_ = bstack1ll111ll_opy_(_1l1l11ll_opy_.get(test.nodeid, None))
    if bstack1l111ll1lll_opy_:
        hook_data[bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭⎰")] = bstack1l111ll1lll_opy_
    if result:
        hook_data[bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⎱")] = result.outcome
        hook_data[bstack11l1l11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⎲")] = result.duration * 1000
        hook_data[bstack11l1l11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎳")] = bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⎴")]
        if result.failed:
            hook_data[bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ⎵")] = bstack1l1lll1l_opy_.bstack11111l111l_opy_(call.excinfo.typename)
            hook_data[bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⎶")] = bstack1l1lll1l_opy_.bstack1llll11ll1ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11l1l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⎷")] = bstack1111lllllll_opy_(outcome)
        hook_data[bstack11l1l11_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ⎸")] = 100
        hook_data[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⎹")] = bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⎺")]
        if hook_data[bstack11l1l11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⎻")] == bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⎼"):
            hook_data[bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭⎽")] = bstack11l1l11_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩ⎾")  # bstack1lll1ll1ll11_opy_
            hook_data[bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ⎿")] = [{bstack11l1l11_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭⏀"): [bstack11l1l11_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨ⏁")]}]
    if bstack1llll11111l1_opy_:
        hook_data[bstack11l1l11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⏂")] = bstack1llll11111l1_opy_.result
        hook_data[bstack11l1l11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ⏃")] = bstack1111l1ll11l_opy_(bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⏄")], bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⏅")])
        hook_data[bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⏆")] = bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⏇")]
        if hook_data[bstack11l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⏈")] == bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ⏉"):
            hook_data[bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ⏊")] = bstack1l1lll1l_opy_.bstack11111l111l_opy_(bstack1llll11111l1_opy_.exception_type)
            hook_data[bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⏋")] = [{bstack11l1l11_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⏌"): bstack111l11l11ll_opy_(bstack1llll11111l1_opy_.exception)}]
    return hook_data
def bstack1llll111l1ll_opy_(test, bstack1l11l11l_opy_, bstack11111111l_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡨࡺࡪࡴࡴ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠡ࠯ࠣࡿࢂ࠭⏍").format(bstack11111111l_opy_))
    bstack1l11lll1_opy_ = bstack1lll1lllll11_opy_(test, bstack1l11l11l_opy_, result, call, bstack11111111l_opy_, outcome)
    driver = getattr(test, bstack11l1l11_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ⏎"), None)
    if bstack11111111l_opy_ == bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⏏") and driver:
        bstack1l11lll1_opy_[bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫ⏐")] = bstack1l1lll1l_opy_.bstack1ll1l1l1_opy_(driver)
    if bstack11111111l_opy_ == bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧ⏑"):
        bstack11111111l_opy_ = bstack11l1l11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⏒")
    bstack1l1l1lll_opy_ = {
        bstack11l1l11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⏓"): bstack11111111l_opy_,
        bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⏔"): bstack1l11lll1_opy_
    }
    bstack1l1lll1l_opy_.bstack1l1lll11_opy_(bstack1l1l1lll_opy_)
    if bstack11111111l_opy_ == bstack11l1l11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫ⏕"):
        threading.current_thread().bstackTestMeta = {bstack11l1l11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⏖"): bstack11l1l11_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⏗")}
    elif bstack11111111l_opy_ == bstack11l1l11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⏘"):
        threading.current_thread().bstackTestMeta = {bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⏙"): getattr(result, bstack11l1l11_opy_ (u"ࠨࡱࡸࡸࡨࡵ࡭ࡦࠩ⏚"), bstack11l1l11_opy_ (u"ࠩࠪ⏛"))}
def bstack1lll1lllllll_opy_(test, bstack1l11l11l_opy_, bstack11111111l_opy_, result=None, call=None, outcome=None, bstack1llll11111l1_opy_=None):
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡷࡪࡴࡤࡠࡪࡲࡳࡰࡥࡲࡶࡰࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥ࡮࡯ࡰ࡭ࠣࡨࡦࡺࡡ࠭ࠢࡨࡺࡪࡴࡴࡕࡻࡳࡩࠥ࠳ࠠࡼࡿࠪ⏜").format(bstack11111111l_opy_))
    hook_data = bstack1llll11111ll_opy_(test, bstack1l11l11l_opy_, bstack11111111l_opy_, result, call, outcome, bstack1llll11111l1_opy_)
    bstack1l1l1lll_opy_ = {
        bstack11l1l11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⏝"): bstack11111111l_opy_,
        bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧ⏞"): hook_data
    }
    bstack1l1lll1l_opy_.bstack1l1lll11_opy_(bstack1l1l1lll_opy_)
def bstack1ll111ll_opy_(bstack1l11l11l_opy_):
    if not bstack1l11l11l_opy_:
        return None
    if bstack1l11l11l_opy_.get(bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ⏟"), None):
        return getattr(bstack1l11l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ⏠")], bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⏡"), None)
    return bstack1l11l11l_opy_.get(bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⏢"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.LOG, bstack1llll1111l1_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_.LOG, bstack1llll1111l1_opy_.POST, request, caplog)
        return # skip all existing operations
    try:
        if not bstack1l1lll1l_opy_.on():
            return
        places = [bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ⏣"), bstack11l1l11_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ⏤"), bstack11l1l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ⏥")]
        logs = []
        for bstack1lll1ll1ll1l_opy_ in places:
            records = caplog.get_records(bstack1lll1ll1ll1l_opy_)
            bstack1llll111l111_opy_ = bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⏦") if bstack1lll1ll1ll1l_opy_ == bstack11l1l11_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ⏧") else bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⏨")
            bstack1lll1lll11l1_opy_ = request.node.nodeid + (bstack11l1l11_opy_ (u"ࠩࠪ⏩") if bstack1lll1ll1ll1l_opy_ == bstack11l1l11_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ⏪") else bstack11l1l11_opy_ (u"ࠫ࠲࠭⏫") + bstack1lll1ll1ll1l_opy_)
            test_uuid = bstack1ll111ll_opy_(_1l1l11ll_opy_.get(bstack1lll1lll11l1_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111l1ll1lll_opy_(record.message):
                    continue
                logs.append({
                    bstack11l1l11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⏬"): bstack111l1l11lll_opy_(record.created).isoformat() + bstack11l1l11_opy_ (u"࡚࠭ࠨ⏭"),
                    bstack11l1l11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⏮"): record.levelname,
                    bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⏯"): record.message,
                    bstack1llll111l111_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1l1lll1l_opy_.bstack1l1l1111_opy_(logs)
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭⏰"), str(err))
def bstack111l11l1l_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1ll1lll_opy_
    bstack1111lll111_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ⏱"), None) and bstack11lll111_opy_(
            threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ⏲"), None)
    bstack111ll1111l_opy_ = getattr(driver, bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ⏳"), None) != None and getattr(driver, bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭⏴"), None) == True
    if sequence == bstack11l1l11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ⏵") and driver != None:
      if not bstack11l1ll1lll_opy_ and bstack1llll11llll_opy_() and bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⏶") in CONFIG and CONFIG[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⏷")] == True and bstack11l1ll11ll_opy_.bstack1ll11l1l11_opy_(driver_command) and (bstack111ll1111l_opy_ or bstack1111lll111_opy_) and not bstack111ll1lll1_opy_(args):
        try:
          bstack11l1ll1lll_opy_ = True
          logger.debug(bstack11l1l11_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬ⏸").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11l1l11_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩ⏹").format(str(err)))
        bstack11l1ll1lll_opy_ = False
    if sequence == bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ⏺"):
        if driver_command == bstack11l1l11_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ⏻"):
            bstack1l1lll1l_opy_.bstack1l11l1lll_opy_({
                bstack11l1l11_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭⏼"): response[bstack11l1l11_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ⏽")],
                bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⏾"): store[bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ⏿")]
            })
def bstack111l1l1l1l_opy_():
    global bstack11llll1l11_opy_
    bstack1ll1111ll_opy_.bstack1l1ll1ll1_opy_()
    logging.shutdown()
    bstack1l1lll1l_opy_.bstack1ll11lll_opy_()
    for driver in bstack11llll1l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1111l11_opy_(*args):
    global bstack11llll1l11_opy_
    bstack1l1lll1l_opy_.bstack1ll11lll_opy_()
    for driver in bstack11llll1l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11l1l1llll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1ll1ll11l_opy_(self, *args, **kwargs):
    bstack111llllll_opy_ = bstack111ll11l11_opy_(self, *args, **kwargs)
    bstack11ll111111_opy_ = getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ␀"), None)
    if bstack11ll111111_opy_ and bstack11ll111111_opy_.get(bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ␁"), bstack11l1l11_opy_ (u"࠭ࠧ␂")) == bstack11l1l11_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ␃"):
        bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
    return bstack111llllll_opy_
@measure(event_name=EVENTS.bstack1l11llll1_opy_, stage=STAGE.bstack111ll111l_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1111l11l1_opy_(framework_name):
    from bstack_utils.config import Config
    bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
    if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ␄")):
        return
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭␅"), True)
    global bstack11l11l1ll_opy_
    global bstack11l1ll11l_opy_
    bstack11l11l1ll_opy_ = framework_name
    logger.info(bstack1lll1l1l1l_opy_.format(bstack11l11l1ll_opy_.split(bstack11l1l11_opy_ (u"ࠪ࠱ࠬ␆"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1llll11llll_opy_():
            Service.start = bstack1l111l111l_opy_
            Service.stop = bstack11lll11l1_opy_
            webdriver.Remote.get = bstack1l1l111ll1_opy_
            webdriver.Remote.__init__ = bstack1l11l1llll_opy_
            if not isinstance(os.getenv(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬ␇")), str):
                return
            WebDriver.quit = bstack11lll111ll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1l1lll1l_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1ll11l_opy_
        bstack11l1ll11l_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11l1l11_opy_ (u"࡙ࠬࡅࡍࡇࡑࡍ࡚ࡓ࡟ࡐࡔࡢࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡊࡐࡖࡘࡆࡒࡌࡆࡆࠪ␈")):
        bstack11l1ll11l_opy_ = eval(os.environ.get(bstack11l1l11_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫ␉")))
    if not bstack11l1ll11l_opy_:
        bstack1l111lll11_opy_(bstack11l1l11_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤ␊"), bstack1l1ll1lll1_opy_)
    if bstack11l11l111l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ␋")) and callable(getattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ␌"))):
                RemoteConnection._get_proxy_url = bstack1ll11ll1l1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack1ll11ll1l1_opy_
        except Exception as e:
            logger.error(bstack1l1llll1ll_opy_.format(str(e)))
    if bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ␍") in str(framework_name).lower():
        if not bstack1llll11llll_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1l11lll11l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1111111_opy_
            Config.getoption = bstack1ll1l1111l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l1lll1l1l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1lll1111l1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack11lll111ll_opy_(self):
    global bstack11l11l1ll_opy_
    global bstack11ll1l1111_opy_
    global bstack1111llll1l_opy_
    try:
        if bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ␎") in bstack11l11l1ll_opy_ and self.session_id != None and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩ␏"), bstack11l1l11_opy_ (u"࠭ࠧ␐")) != bstack11l1l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ␑"):
            bstack1ll1l111l1_opy_ = bstack11l1l11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ␒") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ␓")
            bstack1ll111ll1l_opy_(logger, True)
            if os.environ.get(bstack11l1l11_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭␔"), None):
                self.execute_script(
                    bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ␕") + json.dumps(
                        os.environ.get(bstack11l1l11_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ␖"))) + bstack11l1l11_opy_ (u"࠭ࡽࡾࠩ␗"))
            if self != None:
                bstack11ll1111ll_opy_(self, bstack1ll1l111l1_opy_, bstack11l1l11_opy_ (u"ࠧ࠭ࠢࠪ␘").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1l1ll11l1ll_opy_(bstack1l1l11l11ll_opy_):
            item = store.get(bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ␙"), None)
            if item is not None and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ␚"), None):
                bstack11111l11_opy_.bstack11111ll1_opy_(self, bstack1llll111l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack11l1l11_opy_ (u"ࠪࠫ␛")
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧ␜") + str(e))
    bstack1111llll1l_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1l1lllll1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l11l1llll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11ll1l1111_opy_
    global bstack1111ll11l_opy_
    global bstack11ll1ll1l1_opy_
    global bstack11l11l1ll_opy_
    global bstack111ll11l11_opy_
    global bstack11llll1l11_opy_
    global bstack1ll1l11l1l_opy_
    global bstack111ll1l1l1_opy_
    global bstack1llll111l1_opy_
    CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ␝")] = str(bstack11l11l1ll_opy_) + str(__version__)
    command_executor = bstack1ll111l1l1_opy_(bstack1ll1l11l1l_opy_, CONFIG)
    logger.debug(bstack11l1l1111_opy_.format(command_executor))
    proxy = bstack11l1111ll1_opy_(CONFIG, proxy)
    bstack11111l11l_opy_ = 0
    try:
        if bstack11ll1ll1l1_opy_ is True:
            bstack11111l11l_opy_ = int(os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭␞")))
    except:
        bstack11111l11l_opy_ = 0
    bstack11111ll11_opy_ = bstack111ll1ll11_opy_(CONFIG, bstack11111l11l_opy_)
    logger.debug(bstack1ll1lll1l1_opy_.format(str(bstack11111ll11_opy_)))
    bstack1llll111l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ␟"))[bstack11111l11l_opy_]
    if bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ␠") in CONFIG and CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭␡")]:
        bstack11l1llllll_opy_(bstack11111ll11_opy_, bstack111ll1l1l1_opy_)
    if bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack11111l11l_opy_) and bstack111l1lll_opy_.bstack1ll1ll1l1_opy_(bstack11111ll11_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1l1ll11l1ll_opy_(bstack1l1l11l11ll_opy_):
            bstack111l1lll_opy_.set_capabilities(bstack11111ll11_opy_, CONFIG)
    if desired_capabilities:
        bstack111lll1111_opy_ = bstack1ll1ll1111_opy_(desired_capabilities)
        bstack111lll1111_opy_[bstack11l1l11_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ␢")] = bstack11ll1lllll_opy_(CONFIG)
        bstack1l111l1l1_opy_ = bstack111ll1ll11_opy_(bstack111lll1111_opy_)
        if bstack1l111l1l1_opy_:
            bstack11111ll11_opy_ = update(bstack1l111l1l1_opy_, bstack11111ll11_opy_)
        desired_capabilities = None
    if options:
        bstack1l1l11ll1l_opy_(options, bstack11111ll11_opy_)
    if not options:
        options = bstack11ll111l1l_opy_(bstack11111ll11_opy_)
    if proxy and bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ␣")):
        options.proxy(proxy)
    if options and bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ␤")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack11lll11ll_opy_() < version.parse(bstack11l1l11_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ␥")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11111ll11_opy_)
    logger.info(bstack11l1111111_opy_)
    bstack1l1l1111ll_opy_.end(EVENTS.bstack1l11llll1_opy_.value, EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ␦"),
                               EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ␧"), True, None)
    try:
        if bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ␨")):
            bstack111ll11l11_opy_(self, command_executor=command_executor,
                      options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
        elif bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ␩")):
            bstack111ll11l11_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities, options=options,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        elif bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ␪")):
            bstack111ll11l11_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive, file_detector=file_detector)
        else:
            bstack111ll11l11_opy_(self, command_executor=command_executor,
                      desired_capabilities=desired_capabilities,
                      browser_profile=browser_profile, proxy=proxy,
                      keep_alive=keep_alive)
    except Exception as bstack111llll11l_opy_:
        logger.error(bstack1l1ll11lll_opy_.format(bstack11l1l11_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠫ␫"), str(bstack111llll11l_opy_)))
        raise bstack111llll11l_opy_
    try:
        bstack111ll11lll_opy_ = bstack11l1l11_opy_ (u"࠭ࠧ␬")
        if bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨ␭")):
            bstack111ll11lll_opy_ = self.caps.get(bstack11l1l11_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ␮"))
        else:
            bstack111ll11lll_opy_ = self.capabilities.get(bstack11l1l11_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ␯"))
        if bstack111ll11lll_opy_:
            bstack11l1ll111_opy_(bstack111ll11lll_opy_)
            if bstack11lll11ll_opy_() <= version.parse(bstack11l1l11_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ␰")):
                self.command_executor._url = bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ␱") + bstack1ll1l11l1l_opy_ + bstack11l1l11_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ␲")
            else:
                self.command_executor._url = bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ␳") + bstack111ll11lll_opy_ + bstack11l1l11_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ␴")
            logger.debug(bstack11111ll111_opy_.format(bstack111ll11lll_opy_))
        else:
            logger.debug(bstack111lllll1l_opy_.format(bstack11l1l11_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤ␵")))
    except Exception as e:
        logger.debug(bstack111lllll1l_opy_.format(e))
    bstack11ll1l1111_opy_ = self.session_id
    if bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ␶") in bstack11l11l1ll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11l1l11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ␷"), None)
        if item:
            bstack1lll1llll1l1_opy_ = getattr(item, bstack11l1l11_opy_ (u"ࠫࡤࡺࡥࡴࡶࡢࡧࡦࡹࡥࡠࡵࡷࡥࡷࡺࡥࡥࠩ␸"), False)
            if not getattr(item, bstack11l1l11_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭␹"), None) and bstack1lll1llll1l1_opy_:
                setattr(store[bstack11l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ␺")], bstack11l1l11_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ␻"), self)
        bstack11ll111111_opy_ = getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩ␼"), None)
        if bstack11ll111111_opy_ and bstack11ll111111_opy_.get(bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ␽"), bstack11l1l11_opy_ (u"ࠪࠫ␾")) == bstack11l1l11_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ␿"):
            bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
    bstack11llll1l11_opy_.append(self)
    if bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⑀") in CONFIG and bstack11l1l11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⑁") in CONFIG[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ⑂")][bstack11111l11l_opy_]:
        bstack1111ll11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⑃")][bstack11111l11l_opy_][bstack11l1l11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⑄")]
    logger.debug(bstack1ll1l1ll1_opy_.format(bstack11ll1l1111_opy_))
@measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1l111ll1_opy_(self, url):
    global bstack1ll1lll111_opy_
    global CONFIG
    try:
        bstack11llll1ll1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack11l1l1lll_opy_.format(str(err)))
    try:
        bstack1ll1lll111_opy_(self, url)
    except Exception as e:
        try:
            parsed_error = str(e)
            if any(err_msg in parsed_error for err_msg in bstack11111l111_opy_):
                bstack11llll1ll1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack11l1l1lll_opy_.format(str(err)))
        raise e
def bstack11l1ll111l_opy_(item, when):
    global bstack1llllll1ll_opy_
    try:
        bstack1llllll1ll_opy_(item, when)
    except Exception as e:
        pass
def bstack1l1lll1l1l_opy_(item, call, rep):
    global bstack111ll1111_opy_
    global bstack11llll1l11_opy_
    name = bstack11l1l11_opy_ (u"ࠪࠫ⑅")
    try:
        if rep.when == bstack11l1l11_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ⑆"):
            bstack11ll1l1111_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ⑇"))
            try:
                if (str(skipSessionName).lower() != bstack11l1l11_opy_ (u"࠭ࡴࡳࡷࡨࠫ⑈")):
                    name = str(rep.nodeid)
                    bstack1l1ll1111l_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑉"), name, bstack11l1l11_opy_ (u"ࠨࠩ⑊"), bstack11l1l11_opy_ (u"ࠩࠪ⑋"), bstack11l1l11_opy_ (u"ࠪࠫ⑌"), bstack11l1l11_opy_ (u"ࠫࠬ⑍"))
                    os.environ[bstack11l1l11_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ⑎")] = name
                    for driver in bstack11llll1l11_opy_:
                        if bstack11ll1l1111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll1111l_opy_)
            except Exception as e:
                logger.debug(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭⑏").format(str(e)))
            try:
                bstack1lll11ll11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11l1l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ⑐"):
                    status = bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ⑑") if rep.outcome.lower() == bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⑒") else bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⑓")
                    reason = bstack11l1l11_opy_ (u"ࠫࠬ⑔")
                    if status == bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ⑕"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ⑖") if status == bstack11l1l11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⑗") else bstack11l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ⑘")
                    data = name + bstack11l1l11_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ⑙") if status == bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ⑚") else name + bstack11l1l11_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧ⑛") + reason
                    bstack1l1l11lll1_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ⑜"), bstack11l1l11_opy_ (u"࠭ࠧ⑝"), bstack11l1l11_opy_ (u"ࠧࠨ⑞"), bstack11l1l11_opy_ (u"ࠨࠩ⑟"), level, data)
                    for driver in bstack11llll1l11_opy_:
                        if bstack11ll1l1111_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1l11lll1_opy_)
            except Exception as e:
                logger.debug(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭①").format(str(e)))
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧ②").format(str(e)))
    bstack111ll1111_opy_(item, call, rep)
notset = Notset()
def bstack1ll1l1111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11ll11l1l1_opy_
    if str(name).lower() == bstack11l1l11_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫ③"):
        return bstack11l1l11_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ④")
    else:
        return bstack11ll11l1l1_opy_(self, name, default, skip)
def bstack1ll11ll1l1_opy_(self):
    global CONFIG
    global bstack1lllll11l1_opy_
    try:
        proxy = bstack1l111ll1l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11l1l11_opy_ (u"࠭࠮ࡱࡣࡦࠫ⑤")):
                proxies = bstack1l1ll111ll_opy_(proxy, bstack1ll111l1l1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l11ll1l1_opy_ = proxies.popitem()
                    if bstack11l1l11_opy_ (u"ࠢ࠻࠱࠲ࠦ⑥") in bstack1l11ll1l1_opy_:
                        return bstack1l11ll1l1_opy_
                    else:
                        return bstack11l1l11_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ⑦") + bstack1l11ll1l1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨ⑧").format(str(e)))
    return bstack1lllll11l1_opy_(self)
def bstack11l11l111l_opy_():
    return (bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭⑨") in CONFIG or bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ⑩") in CONFIG) and bstack11111lll1_opy_() and bstack11lll11ll_opy_() >= version.parse(
        bstack1ll1l1l111_opy_)
def bstack11111l1ll_opy_(self,
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
    global bstack1111ll11l_opy_
    global bstack11ll1ll1l1_opy_
    global bstack11l11l1ll_opy_
    CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ⑪")] = str(bstack11l11l1ll_opy_) + str(__version__)
    bstack11111l11l_opy_ = 0
    try:
        if bstack11ll1ll1l1_opy_ is True:
            bstack11111l11l_opy_ = int(os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭⑫")))
    except:
        bstack11111l11l_opy_ = 0
    CONFIG[bstack11l1l11_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ⑬")] = True
    bstack11111ll11_opy_ = bstack111ll1ll11_opy_(CONFIG, bstack11111l11l_opy_)
    logger.debug(bstack1ll1lll1l1_opy_.format(str(bstack11111ll11_opy_)))
    if CONFIG.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ⑭")):
        bstack11l1llllll_opy_(bstack11111ll11_opy_, bstack111ll1l1l1_opy_)
    if bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⑮") in CONFIG and bstack11l1l11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⑯") in CONFIG[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⑰")][bstack11111l11l_opy_]:
        bstack1111ll11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⑱")][bstack11111l11l_opy_][bstack11l1l11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⑲")]
    import urllib
    import json
    if bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⑳") in CONFIG and str(CONFIG[bstack11l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⑴")]).lower() != bstack11l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ⑵"):
        bstack1111lll11_opy_ = bstack111l11l1ll_opy_()
        bstack1ll1ll1l1l_opy_ = bstack1111lll11_opy_ + urllib.parse.quote(json.dumps(bstack11111ll11_opy_))
    else:
        bstack1ll1ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ⑶") + urllib.parse.quote(json.dumps(bstack11111ll11_opy_))
    browser = self.connect(bstack1ll1ll1l1l_opy_)
    return browser
def bstack11l1l11ll_opy_():
    global bstack11l1ll11l_opy_
    global bstack11l11l1ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11111ll1l1_opy_
        if not bstack1llll11llll_opy_():
            global bstack11l1lll1l1_opy_
            if not bstack11l1lll1l1_opy_:
                from bstack_utils.helper import bstack1lll11ll1l_opy_, bstack11l1ll11l1_opy_
                bstack11l1lll1l1_opy_ = bstack1lll11ll1l_opy_()
                bstack11l1ll11l1_opy_(bstack11l11l1ll_opy_)
            BrowserType.connect = bstack11111ll1l1_opy_
            return
        BrowserType.launch = bstack11111l1ll_opy_
        bstack11l1ll11l_opy_ = True
    except Exception as e:
        pass
def bstack1lll1lll11ll_opy_():
    global CONFIG
    global bstack11l1l1111l_opy_
    global bstack1ll1l11l1l_opy_
    global bstack111ll1l1l1_opy_
    global bstack11ll1ll1l1_opy_
    global bstack1l1l111lll_opy_
    CONFIG = json.loads(os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪ⑷")))
    bstack11l1l1111l_opy_ = eval(os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭⑸")))
    bstack1ll1l11l1l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭⑹"))
    bstack11111l1ll1_opy_(CONFIG, bstack11l1l1111l_opy_)
    bstack1l1l111lll_opy_ = bstack1ll1111ll_opy_.configure_logger(CONFIG, bstack1l1l111lll_opy_)
    if cli.bstack1ll1l1l1l_opy_():
        bstack11l11lllll_opy_.invoke(Events.CONNECT, bstack111llll1ll_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ⑺"), bstack11l1l11_opy_ (u"ࠨ࠲ࠪ⑻")))
        cli.bstack1l11lll1l1l_opy_(cli_context.platform_index)
        cli.bstack1l1l1ll1l11_opy_(bstack1ll111l1l1_opy_(bstack1ll1l11l1l_opy_, CONFIG), cli_context.platform_index, bstack11ll111l1l_opy_)
        cli.bstack1l11lllllll_opy_()
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡆࡐࡎࠦࡩࡴࠢࡤࡧࡹ࡯ࡶࡦࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣ⑼") + str(cli_context.platform_index) + bstack11l1l11_opy_ (u"ࠥࠦ⑽"))
        return # skip all existing operations
    global bstack111ll11l11_opy_
    global bstack1111llll1l_opy_
    global bstack11111l1l1_opy_
    global bstack1lll11l111_opy_
    global bstack11l11llll1_opy_
    global bstack1l1111l1l_opy_
    global bstack11111ll1l_opy_
    global bstack1ll1lll111_opy_
    global bstack1lllll11l1_opy_
    global bstack11ll11l1l1_opy_
    global bstack1llllll1ll_opy_
    global bstack111ll1111_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack111ll11l11_opy_ = webdriver.Remote.__init__
        bstack1111llll1l_opy_ = WebDriver.quit
        bstack11111ll1l_opy_ = WebDriver.close
        bstack1ll1lll111_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ⑾") in CONFIG or bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ⑿") in CONFIG) and bstack11111lll1_opy_():
        if bstack11lll11ll_opy_() < version.parse(bstack1ll1l1l111_opy_):
            logger.error(bstack1l11ll1ll1_opy_.format(bstack11lll11ll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack11l1l11_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ⒀")) and callable(getattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ⒁"))):
                    bstack1lllll11l1_opy_ = RemoteConnection._get_proxy_url
                else:
                    from selenium.webdriver.remote.client_config import ClientConfig
                    bstack1lllll11l1_opy_ = ClientConfig.get_proxy_url
            except Exception as e:
                logger.error(bstack1l1llll1ll_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11ll11l1l1_opy_ = Config.getoption
        from _pytest import runner
        bstack1llllll1ll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack111l11ll_opy_)
    try:
        from pytest_bdd import reporting
        bstack111ll1111_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ⒂"))
    bstack111ll1l1l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭⒃"), {}).get(bstack11l1l11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ⒄"))
    bstack11ll1ll1l1_opy_ = True
    bstack1111l11l1_opy_(bstack1ll1ll1ll1_opy_)
if (bstack111l11lll11_opy_()):
    bstack1lll1lll11ll_opy_()
@error_handler(class_method=False)
def bstack1llll1111lll_opy_(hook_name, event, bstack1ll1l111l11_opy_=None):
    if hook_name not in [bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ⒅"), bstack11l1l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ⒆"), bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ⒇"), bstack11l1l11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ⒈"), bstack11l1l11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭⒉"), bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ⒊"), bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩ⒋"), bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭⒌")]:
        return
    node = store[bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ⒍")]
    if hook_name in [bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ⒎"), bstack11l1l11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ⒏")]:
        node = store[bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧ⒐")]
    elif hook_name in [bstack11l1l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ⒑"), bstack11l1l11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ⒒")]:
        node = store[bstack11l1l11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩ⒓")]
    hook_type = bstack11l111lll11_opy_(hook_name)
    if event == bstack11l1l11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ⒔"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_[hook_type], bstack1llll1111l1_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack1lll111l_opy_ = {
            bstack11l1l11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⒕"): uuid,
            bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⒖"): bstack1ll1ll11_opy_(),
            bstack11l1l11_opy_ (u"ࠨࡶࡼࡴࡪ࠭⒗"): bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⒘"),
            bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭⒙"): hook_type,
            bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧ⒚"): hook_name
        }
        store[bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ⒛")].append(uuid)
        bstack1llll111ll11_opy_ = node.nodeid
        if hook_type == bstack11l1l11_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ⒜"):
            if not _1l1l11ll_opy_.get(bstack1llll111ll11_opy_, None):
                _1l1l11ll_opy_[bstack1llll111ll11_opy_] = {bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⒝"): []}
            _1l1l11ll_opy_[bstack1llll111ll11_opy_][bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⒞")].append(bstack1lll111l_opy_[bstack11l1l11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⒟")])
        _1l1l11ll_opy_[bstack1llll111ll11_opy_ + bstack11l1l11_opy_ (u"ࠪ࠱ࠬ⒠") + hook_name] = bstack1lll111l_opy_
        bstack1lll1lllllll_opy_(node, bstack1lll111l_opy_, bstack11l1l11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⒡"))
    elif event == bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫ⒢"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1lll1lllll1_opy_[hook_type], bstack1llll1111l1_opy_.POST, node, None, bstack1ll1l111l11_opy_)
            return
        bstack1l111111_opy_ = node.nodeid + bstack11l1l11_opy_ (u"࠭࠭ࠨ⒣") + hook_name
        _1l1l11ll_opy_[bstack1l111111_opy_][bstack11l1l11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⒤")] = bstack1ll1ll11_opy_()
        bstack1lll1lllll1l_opy_(_1l1l11ll_opy_[bstack1l111111_opy_][bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⒥")])
        bstack1lll1lllllll_opy_(node, _1l1l11ll_opy_[bstack1l111111_opy_], bstack11l1l11_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⒦"), bstack1llll11111l1_opy_=bstack1ll1l111l11_opy_)
def bstack1lll1ll1lll1_opy_():
    global bstack1lll1lll1l1l_opy_
    if bstack11ll1ll11_opy_():
        bstack1lll1lll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧ⒧")
    else:
        bstack1lll1lll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⒨")
def pytest_collection_modifyitems(session, config, items):
    bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡌࡩ࡭ࡶࡨࡶࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡳࡽࡹ࡫ࡳࡵࠢ࡬ࡸࡪࡳࡳࠡࡤࡤࡷࡪࡪࠠࡰࡰࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡶࡩࡱ࡫ࡣࡵࡱࡵࡷࠥ࡬ࡲࡰ࡯ࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡸࡶࡦࡴ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ⒩")
    import os
    bstack1lll1llll111_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡕࡒࡄࡊࡈࡗ࡙ࡘࡁࡕࡇࡇࡣࡘࡋࡌࡆࡅࡗࡓࡗ࡙ࠧ⒪"))
    if not bstack1lll1llll111_opy_:
        return
    try:
        bstack1lll1llll11l_opy_ = json.loads(bstack1lll1llll111_opy_)
        if not isinstance(bstack1lll1llll11l_opy_, (list, set)) or not bstack1lll1llll11l_opy_:
            return
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡄࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡴࡦࡸࡳࡦࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕ࠽ࠤࠧ⒫") + str(e) + bstack11l1l11_opy_ (u"ࠣࠤ⒬"))
        return
    selected = []
    deselected = []
    bstack1llll111l11l_opy_ = set()
    for selector in bstack1lll1llll11l_opy_:
        if not selector or not isinstance(selector, str):
            continue
        bstack1llll111l11l_opy_.add(selector)
    for item in items:
        nodeid = getattr(item, bstack11l1l11_opy_ (u"ࠩࡱࡳࡩ࡫ࡩࡥࠩ⒭"), None)
        if not nodeid:
            deselected.append(item)
            continue
        if (
            nodeid in bstack1llll111l11l_opy_ or
            any(sel in nodeid for sel in bstack1llll111l11l_opy_)
        ):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
@bstack1l1lll1l_opy_.bstack1llll1l1ll11_opy_
def bstack1lll1lll1ll1_opy_():
    bstack1lll1ll1lll1_opy_()
    if cli.is_running():
        try:
            bstack11l1l1lllll_opy_(bstack1llll1111lll_opy_)
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࡳࠡࡲࡤࡸࡨ࡮࠺ࠡࡽࢀࠦ⒮").format(e))
        return
    if bstack11111lll1_opy_():
        bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
        bstack11l1l11_opy_ (u"ࠫࠬ࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡳࡴࡵࠦ࠽ࠡ࠳࠯ࠤࡲࡵࡤࡠࡧࡻࡩࡨࡻࡴࡦࠢࡪࡩࡹࡹࠠࡶࡵࡨࡨࠥ࡬࡯ࡳࠢࡤ࠵࠶ࡿࠠࡤࡱࡰࡱࡦࡴࡤࡴ࠯ࡺࡶࡦࡶࡰࡪࡰࡪࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡉࡳࡷࠦࡰࡱࡲࠣࡂࠥ࠷ࠬࠡ࡯ࡲࡨࡤ࡫ࡸࡦࡥࡸࡸࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡴࡸࡲࠥࡨࡥࡤࡣࡸࡷࡪࠦࡩࡵࠢ࡬ࡷࠥࡶࡡࡵࡥ࡫ࡩࡩࠦࡩ࡯ࠢࡤࠤࡩ࡯ࡦࡧࡧࡵࡩࡳࡺࠠࡱࡴࡲࡧࡪࡹࡳࠡ࡫ࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡺࡹࠠࡸࡧࠣࡲࡪ࡫ࡤࠡࡶࡲࠤࡺࡹࡥࠡࡕࡨࡰࡪࡴࡩࡶ࡯ࡓࡥࡹࡩࡨࠩࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡬ࡦࡴࡤ࡭ࡧࡵ࠭ࠥ࡬࡯ࡳࠢࡳࡴࡵࠦ࠾ࠡ࠳ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬ࠭ࠧ⒯")
        if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩ⒰")):
            if CONFIG.get(bstack11l1l11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭⒱")) is not None and int(CONFIG[bstack11l1l11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ⒲")]) > 1:
                bstack1l1lll1ll_opy_(bstack111l11l1l_opy_)
            return
        bstack1l1lll1ll_opy_(bstack111l11l1l_opy_)
    try:
        bstack11l1l1lllll_opy_(bstack1llll1111lll_opy_)
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡸࠦࡰࡢࡶࡦ࡬࠿ࠦࡻࡾࠤ⒳").format(e))
bstack1lll1lll1ll1_opy_()