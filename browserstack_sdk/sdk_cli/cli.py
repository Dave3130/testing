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
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import bstack1l1l111111l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1l1ll1_opy_ import bstack1l1ll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1l1l111l111_opy_ import bstack1l1l11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack1lllllll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll11l1_opy_ import bstack1ll1lll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1l11llll111_opy_ import bstack1l1l11l11ll_opy_
from browserstack_sdk.sdk_cli.bstack11l11lllll_opy_ import bstack11l11lllll_opy_, Events, bstack111llll1ll_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1l1llll_opy_ import bstack1l11lll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import bstack1lll11ll111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll1ll11l1_opy_
from bstack_utils.helper import Notset, bstack1l1l1lllll1_opy_, get_cli_dir, bstack1l1l1111111_opy_, bstack11ll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1l_opy_ import bstack1ll1l11111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1111111l1_opy_ import bstack1111l1l111_opy_
from bstack_utils.helper import Notset, bstack1l1l1lllll1_opy_, get_cli_dir, bstack1l1l1111111_opy_, bstack11ll1ll11_opy_, bstack11lll1llll_opy_, bstack1111l11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lllll1_opy_, bstack1lll1l1ll11_opy_, bstack1llll1111l1_opy_, bstack1ll111l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import bstack1111111111_opy_, bstack1llll1l1lll_opy_, bstack1111111l1l_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1lll11l1l1_opy_ import bstack1l11l1l1ll_opy_
from bstack_utils import bstack1ll1111ll_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1ll1ll1l_opy_, bstack1ll1111lll_opy_
logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1ll1111ll_opy_.bstack1l1l111llll_opy_())
def bstack1l1l11l11l1_opy_(bs_config):
    bstack1l1ll11111l_opy_ = None
    bstack1l1l111l1ll_opy_ = None
    try:
        bstack1l1l111l1ll_opy_ = get_cli_dir()
        bstack1l1ll11111l_opy_ = bstack1l1l1111111_opy_(bstack1l1l111l1ll_opy_)
        bstack1l1l1l1ll11_opy_ = bstack1l1l1lllll1_opy_(bstack1l1ll11111l_opy_, bstack1l1l111l1ll_opy_, bs_config)
        bstack1l1ll11111l_opy_ = bstack1l1l1l1ll11_opy_ if bstack1l1l1l1ll11_opy_ else bstack1l1ll11111l_opy_
        if not bstack1l1ll11111l_opy_:
            raise ValueError(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠢዡ"))
    except Exception as ex:
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡱࡧࡴࡦࡵࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࢀࢃࠢዢ").format(ex))
        bstack1l1ll11111l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣዣ"))
        if bstack1l1ll11111l_opy_:
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡆࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡕࡇࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡐࡂࡖࡋࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠺ࠡࠤዤ") + str(bstack1l1ll11111l_opy_) + bstack11l1l11_opy_ (u"ࠢࠣዥ"))
        else:
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡐࡲࠤࡻࡧ࡬ࡪࡦࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡧࡱࡺ࡮ࡸ࡯࡯࡯ࡨࡲࡹࡁࠠࡴࡧࡷࡹࡵࠦ࡭ࡢࡻࠣࡦࡪࠦࡩ࡯ࡥࡲࡱࡵࡲࡥࡵࡧ࠱ࠦዦ"))
    return bstack1l1ll11111l_opy_, bstack1l1l111l1ll_opy_
bstack1l1l1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠤ࠼࠽࠾࠿ࠢዧ")
bstack1l1l1ll11l1_opy_ = bstack11l1l11_opy_ (u"ࠥࡶࡪࡧࡤࡺࠤየ")
bstack1l1l1lll1ll_opy_ = bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡘࡋࡓࡔࡋࡒࡒࡤࡏࡄࠣዩ")
bstack1l1l111lll1_opy_ = bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡒࡉࡔࡖࡈࡒࡤࡇࡄࡅࡔࠥዪ")
bstack11l1l1ll1_opy_ = bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠤያ")
bstack1l1l1l11l1l_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡲࠣࠪࡂ࡭࠮࠴ࠪࠩࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑࡼࡃࡕࠬ࠲࠯ࠨዬ"))
bstack1l1l1l1111l_opy_ = bstack11l1l11_opy_ (u"ࠣࡦࡨࡺࡪࡲ࡯ࡱ࡯ࡨࡲࡹࠨይ")
bstack1l1l11llll1_opy_ = bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡒࡖࡈࡋ࡟ࡇࡃࡏࡐࡇࡇࡃࡌࠤዮ")
bstack1l11ll1ll1l_opy_ = [
    Events.bstack111l111lll_opy_,
    Events.CONNECT,
    Events.bstack1lll11llll_opy_,
]
class SDKCLI:
    _1ll1ll1l111_opy_ = None
    process: Union[None, Any]
    bstack1l1l11lll11_opy_: bool
    bstack1l11lllll11_opy_: bool
    bstack1l1l1lll1l1_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l11ll1l1_opy_: Union[None, grpc.Channel]
    bstack1l1l11l1ll1_opy_: str
    test_framework: TestFramework
    bstack1llllll111l_opy_: bstack1lll11ll111_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l111ll11_opy_: bstack1l1l11l11ll_opy_
    accessibility: bstack1l1l111111l_opy_
    bstack1111111l1_opy_: bstack1111l1l111_opy_
    ai: bstack1l1ll1l1111_opy_
    bstack1l1l1ll111l_opy_: bstack1l1l11l111l_opy_
    bstack1l1l1llll11_opy_: List[bstack1lllll1l111_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1ll1ll1_opy_: Any
    bstack1l1l11ll111_opy_: Dict[str, timedelta]
    bstack1l1l1l11lll_opy_: str
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    def __new__(cls):
        if not cls._1ll1ll1l111_opy_:
            cls._1ll1ll1l111_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll1l111_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l11lll11_opy_ = False
        self.bstack1l1l11ll1l1_opy_ = None
        self.bstack1llll1ll11l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l111lll1_opy_, None)
        self.bstack1l1l1llllll_opy_ = os.environ.get(bstack1l1l1lll1ll_opy_, bstack11l1l11_opy_ (u"ࠥࠦዯ")) == bstack11l1l11_opy_ (u"ࠦࠧደ")
        self.bstack1l11lllll11_opy_ = False
        self.bstack1l1l1lll1l1_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1ll1ll1_opy_ = None
        self.test_framework = None
        self.bstack1llllll111l_opy_ = None
        self.bstack1l1l11l1ll1_opy_=bstack11l1l11_opy_ (u"ࠧࠨዱ")
        self.session_framework = None
        self.logger = bstack1ll1111ll_opy_.get_logger(self.__class__.__name__, bstack1ll1111ll_opy_.bstack1l1l111llll_opy_())
        self.bstack1l1l11ll111_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll1l11111_opy_ = bstack1lll11lllll_opy_()
        self.bstack1l11ll1llll_opy_ = None
        self.bstack1ll1llll11l_opy_ = None
        self.bstack1l1l111ll11_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1llll11_opy_ = []
    def bstack1l1l11l1ll_opy_(self):
        return os.environ.get(bstack11l1l1ll1_opy_).lower().__eq__(bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦዲ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l11llll1_opy_, bstack11l1l11_opy_ (u"ࠧࠨዳ")).lower() in [bstack11l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ዴ"), bstack11l1l11_opy_ (u"ࠩ࠴ࠫድ"), bstack11l1l11_opy_ (u"ࠪࡽࡪࡹࠧዶ")]:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡋࡵࡲࡤ࡫ࡱ࡫ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠ࡮ࡱࡧࡩࠥࡪࡵࡦࠢࡷࡳࠥࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡕࡒࡄࡇࡢࡊࡆࡒࡌࡃࡃࡆࡏࠥ࡫࡮ࡷ࡫ࡵࡳࡳࡳࡥ࡯ࡶࠣࡺࡦࡸࡩࡢࡤ࡯ࡩࠧዷ"))
            os.environ[bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡎ࡙࡟ࡓࡗࡑࡒࡎࡔࡇࠣዸ")] = bstack11l1l11_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧዹ")
            return False
        if bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫዺ") in config and str(config[bstack11l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬዻ")]).lower() != bstack11l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨዼ"):
            return False
        bstack1l1ll11l11l_opy_ = [bstack11l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥዽ"), bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣዾ")]
        bstack1l1l1ll11ll_opy_ = config.get(bstack11l1l11_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣዿ")) in bstack1l1ll11l11l_opy_ or os.environ.get(bstack11l1l11_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧጀ")) in bstack1l1ll11l11l_opy_
        os.environ[bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡉࡔࡡࡕ࡙ࡓࡔࡉࡏࡉࠥጁ")] = str(bstack1l1l1ll11ll_opy_) # bstack1l1l111l11l_opy_ bstack1l1ll1111ll_opy_ VAR to bstack1l11ll1lll1_opy_ is binary running
        return bstack1l1l1ll11ll_opy_
    def bstack111llllll1_opy_(self):
        for event in bstack1l11ll1ll1l_opy_:
            bstack11l11lllll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack11l11lllll_opy_.logger.debug(bstack11l1l11_opy_ (u"ࠣࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠠ࠾ࡀࠣࡿࡦࡸࡧࡴࡿࠣࠦጂ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠤࠥጃ"))
            )
        bstack11l11lllll_opy_.register(Events.bstack111l111lll_opy_, self.__1l1l1l1lll1_opy_)
        bstack11l11lllll_opy_.register(Events.CONNECT, self.__1l1ll1111l1_opy_)
        bstack11l11lllll_opy_.register(Events.bstack1lll11llll_opy_, self.__1l1l11lll1l_opy_)
        bstack11l11lllll_opy_.register(Events.bstack1ll1l11l1_opy_, self.__1l1ll111ll1_opy_)
    def bstack1ll1l1l1l_opy_(self):
        return not self.bstack1l1l1llllll_opy_ and os.environ.get(bstack1l1l1lll1ll_opy_, bstack11l1l11_opy_ (u"ࠥࠦጄ")) != bstack11l1l11_opy_ (u"ࠦࠧጅ")
    def is_running(self):
        if self.bstack1l1l1llllll_opy_:
            return self.bstack1l1l11lll11_opy_
        else:
            return bool(self.bstack1l1l11ll1l1_opy_)
    def bstack1l1ll11l1ll_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1llll11_opy_) and cli.is_running()
    def __1l1ll11ll1l_opy_(self, bstack1l1ll111lll_opy_=10):
        if self.bstack1llll1ll11l_opy_:
            return
        bstack1l11lll1l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l111lll1_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡡࠢጆ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠨ࡝ࠡࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡱ࡫ࠧጇ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11l1l11_opy_ (u"ࠢࡨࡴࡳࡧ࠳࡫࡮ࡢࡤ࡯ࡩࡤ࡮ࡴࡵࡲࡢࡴࡷࡵࡸࡺࠤገ"), 0), (bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡷࡤࡶࡲࡰࡺࡼࠦጉ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1ll111lll_opy_)
        self.bstack1l1l11ll1l1_opy_ = channel
        self.bstack1llll1ll11l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l11ll1l1_opy_)
        self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࠣጊ"), datetime.now() - bstack1l11lll1l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l111lll1_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨ࠿ࠦࡩࡴࡡࡦ࡬࡮ࡲࡤࡠࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥጋ") + str(self.bstack1ll1l1l1l_opy_()) + bstack11l1l11_opy_ (u"ࠦࠧጌ"))
    def __1l1l11lll1l_opy_(self, event_name):
        if self.bstack1ll1l1l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡱࡳࡴ࡮ࡴࡧࠡࡅࡏࡍࠧግ"))
        self.__1l1l1l11ll1_opy_()
    def __1l1ll111ll1_opy_(self, event_name, bstack1l11llll11l_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack11l1l11_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠨጎ"))
        bstack1l1ll11l1l1_opy_ = Path(bstack1llll1111_opy_ (u"ࠢࡼࡵࡨࡰ࡫࠴ࡣ࡭࡫ࡢࡨ࡮ࡸࡽ࠰ࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࡵ࠱࡮ࡸࡵ࡮ࠣጏ"))
        if self.bstack1l1l111l1ll_opy_ and bstack1l1ll11l1l1_opy_.exists():
            with open(bstack1l1ll11l1l1_opy_, bstack11l1l11_opy_ (u"ࠨࡴࠪጐ"), encoding=bstack11l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ጑")) as fp:
                data = json.load(fp)
                try:
                    bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨጒ"), bstack1l11l1l1ll_opy_(bstack1lll111l11_opy_), data, {
                        bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡩࠩጓ"): (self.config[bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧጔ")], self.config[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩጕ")])
                    })
                except Exception as e:
                    logger.debug(bstack1ll1111lll_opy_.format(str(e)))
            bstack1l1ll11l1l1_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l1llll1l_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1l1l1lll1_opy_(self, event_name: str, data):
        from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
        self.bstack1l1l11l1ll1_opy_, self.bstack1l1l111l1ll_opy_ = bstack1l1l11l11l1_opy_(data.bs_config)
        os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡗࡓࡋࡗࡅࡇࡒࡅࡠࡆࡌࡖࠬ጖")] = self.bstack1l1l111l1ll_opy_
        if not self.bstack1l1l11l1ll1_opy_ or not self.bstack1l1l111l1ll_opy_:
            raise ValueError(bstack11l1l11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡇࡑࡏࠠࡣ࡫ࡱࡥࡷࡿࠢ጗"))
        if self.bstack1ll1l1l1l_opy_():
            self.__1l1ll1111l1_opy_(event_name, bstack111llll1ll_opy_())
            return
        try:
            bstack111111111l_opy_.end(EVENTS.bstack1l11llll1_opy_.value, EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤጘ"), EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣጙ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡈࡵ࡭ࡱ࡮ࡨࡸࡪࠦࡓࡅࡍࠣࡗࡪࡺࡵࡱ࠰ࠥጚ"))
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡻࡾࠤጛ").format(e))
        start = datetime.now()
        is_started = self.__1l1l11l1l11_opy_()
        self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡳࡱࡣࡺࡲࡤࡺࡩ࡮ࡧࠥጜ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1ll11ll1l_opy_()
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨጝ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l11lllll_opy_(data)
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨጞ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l1l111l1_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1ll1111l1_opy_(self, event_name: str, data: bstack111llll1ll_opy_):
        if not self.bstack1ll1l1l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡯ࡰࡨࡧࡹࡀࠠ࡯ࡱࡷࠤࡦࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨጟ"))
            return
        bin_session_id = os.environ.get(bstack1l1l1lll1ll_opy_)
        start = datetime.now()
        self.__1l1ll11ll1l_opy_()
        self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤጠ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠠࡵࡱࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡉࡌࡊࠢࠥጡ") + str(bin_session_id) + bstack11l1l11_opy_ (u"ࠧࠨጢ"))
        start = datetime.now()
        self.__1l1l1l1l11l_opy_()
        self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦጣ"), datetime.now() - start)
    def __1l11lll1ll1_opy_(self):
        if not self.bstack1llll1ll11l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡤࡣࡱࡲࡴࡺࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࠣࡱࡴࡪࡵ࡭ࡧࡶࠦጤ"))
            return
        bstack1l1l1ll1l1l_opy_ = {
            bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧጥ"): (bstack1ll1lll1ll1_opy_, bstack1lll1ll11ll_opy_, bstack1lll1ll11l1_opy_),
            bstack11l1l11_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦጦ"): (bstack1lllllll11l_opy_, bstack1lll111lll1_opy_, bstack1llllll11l1_opy_),
        }
        if not self.bstack1l11ll1llll_opy_ and self.session_framework in bstack1l1l1ll1l1l_opy_:
            bstack1l1l111l1l1_opy_, bstack1l11lll11ll_opy_, bstack1l1l1l1ll1l_opy_ = bstack1l1l1ll1l1l_opy_[self.session_framework]
            bstack1l1ll111l1l_opy_ = bstack1l11lll11ll_opy_()
            self.bstack1ll1llll11l_opy_ = bstack1l1ll111l1l_opy_
            self.bstack1l11ll1llll_opy_ = bstack1l1l1l1ll1l_opy_
            self.bstack1l1l1llll11_opy_.append(bstack1l1ll111l1l_opy_)
            self.bstack1l1l1llll11_opy_.append(bstack1l1l111l1l1_opy_(self.bstack1ll1llll11l_opy_))
        if not self.bstack1l1l111ll11_opy_ and self.config_observability and self.config_observability.success: # bstack1llll1ll1l1_opy_
            self.bstack1l1l111ll11_opy_ = bstack1l1l11l11ll_opy_(self.bstack1l11ll1llll_opy_, self.bstack1ll1llll11l_opy_) # bstack1l11llll1ll_opy_
            self.bstack1l1l1llll11_opy_.append(self.bstack1l1l111ll11_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l111111l_opy_(self.bstack1l11ll1llll_opy_, self.bstack1ll1llll11l_opy_)
            self.bstack1l1l1llll11_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11l1l11_opy_ (u"ࠥࡷࡪࡲࡦࡉࡧࡤࡰࠧጧ"), False) == True:
            self.ai = bstack1l1ll1l1111_opy_()
            self.bstack1l1l1llll11_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1ll1ll1_opy_ and self.bstack1l1l1ll1ll1_opy_.success:
            self.percy = bstack1l1l11l111l_opy_(self.bstack1l1l1ll1ll1_opy_)
            self.bstack1l1l1llll11_opy_.append(self.percy)
        for mod in self.bstack1l1l1llll11_opy_:
            if not mod.bstack1lll11llll1_opy_():
                mod.configure(self.bstack1llll1ll11l_opy_, self.config, self.cli_bin_session_id, self.bstack1lll1l11111_opy_)
    def __1l1l1l11111_opy_(self):
        for mod in self.bstack1l1l1llll11_opy_:
            if mod.bstack1lll11llll1_opy_():
                mod.configure(self.bstack1llll1ll11l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11llllll1_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1l11lllll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l11lllll11_opy_:
            return
        self.__1l1l1111l1l_opy_(data)
        bstack1l11lll1l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦጨ")
        req.sdk_language = bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧጩ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l1l11l1l_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࠣጪ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨጫ"))
            r = self.bstack1llll1ll11l_opy_.StartBinSession(req)
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥጬ"), datetime.now() - bstack1l11lll1l_opy_)
            os.environ[bstack1l1l1lll1ll_opy_] = r.bin_session_id
            self.__1l1l11l1l1l_opy_(r)
            self.__1l11lll1ll1_opy_()
            self.bstack1lll1l11111_opy_.start()
            self.bstack1l11lllll11_opy_ = True
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞ࠦጭ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠣጮ"))
        except grpc.bstack1l1l1111l11_opy_ as bstack1l1l1111lll_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨጯ") + str(bstack1l1l1111lll_opy_) + bstack11l1l11_opy_ (u"ࠧࠨጰ"))
            traceback.print_exc()
            raise bstack1l1l1111lll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጱ") + str(e) + bstack11l1l11_opy_ (u"ࠢࠣጲ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l11ll11l_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1l1l1l11l_opy_(self):
        if not self.bstack1ll1l1l1l_opy_() or not self.cli_bin_session_id or self.bstack1l1l1lll1l1_opy_:
            return
        bstack1l11lll1l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨጳ"), bstack11l1l11_opy_ (u"ࠩ࠳ࠫጴ")))
        try:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࠧጵ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨጶ"))
            r = self.bstack1llll1ll11l_opy_.ConnectBinSession(req)
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤጷ"), datetime.now() - bstack1l11lll1l_opy_)
            self.__1l1l11l1l1l_opy_(r)
            self.__1l11lll1ll1_opy_()
            self.bstack1lll1l11111_opy_.start()
            self.bstack1l1l1lll1l1_opy_ = True
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࠣጸ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨጹ"))
        except grpc.bstack1l1l1111l11_opy_ as bstack1l1l1111lll_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጺ") + str(bstack1l1l1111lll_opy_) + bstack11l1l11_opy_ (u"ࠤࠥጻ"))
            traceback.print_exc()
            raise bstack1l1l1111lll_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢጼ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧጽ"))
            traceback.print_exc()
            raise e
    def __1l1l11l1l1l_opy_(self, r):
        self.bstack1l1ll111111_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11l1l11_opy_ (u"ࠧࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡶࡩࡷࡼࡥࡳࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦጾ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11l1l11_opy_ (u"ࠨࡥ࡮ࡲࡷࡽࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬࡯ࡶࡰࡧࠦጿ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕ࡫ࡲࡤࡻࠣ࡭ࡸࠦࡳࡦࡰࡷࠤࡴࡴ࡬ࡺࠢࡤࡷࠥࡶࡡࡳࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࠦࡈࡵ࡮࡯ࡧࡦࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠭ࠤࠣࡥࡳࡪࠠࡵࡪ࡬ࡷࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡪࡵࠣࡥࡱࡹ࡯ࠡࡷࡶࡩࡩࠦࡢࡺࠢࡖࡸࡦࡸࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࡵࡩ࡫ࡵࡲࡦ࠮ࠣࡒࡴࡴࡥࠡࡪࡤࡲࡩࡲࡩ࡯ࡩࠣ࡭ࡸࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤፀ")
        self.bstack1l1l1ll1ll1_opy_ = getattr(r, bstack11l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧፁ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ፂ")] = self.config_testhub.jwt
        os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨፃ")] = self.config_testhub.build_hashed_id
    def bstack1l1l1l1l111_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l11lll11_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l11111l1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l11111l1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l1l1l111_opy_(event_name=EVENTS.bstack1l11lllll1l_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1l11l1l11_opy_(self, bstack1l1ll111lll_opy_=10):
        if self.bstack1l1l11lll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡸࡺࡡࡳࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨፄ"))
            return True
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡹࡴࡢࡴࡷࠦፅ"))
        if os.getenv(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡈࡒ࡛ࠨፆ")) == bstack1l1l1l1111l_opy_:
            self.cli_bin_session_id = bstack1l1l1l1111l_opy_
            self.cli_listen_addr = bstack11l1l11_opy_ (u"ࠢࡶࡰ࡬ࡼ࠿࠵ࡴ࡮ࡲ࠲ࡷࡩࡱ࠭ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯ࠨࡷ࠳ࡹ࡯ࡤ࡭ࠥፇ") % (self.cli_bin_session_id)
            self.bstack1l1l11lll11_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l11l1ll1_opy_, bstack11l1l11_opy_ (u"ࠣࡵࡧ࡯ࠧፈ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l11lll111l_opy_ compat for text=True in bstack1l1ll11l111_opy_ python
            encoding=bstack11l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣፉ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1l11ll1ll_opy_ = threading.Thread(target=self.__1l1l1l1l1ll_opy_, args=(bstack1l1ll111lll_opy_,))
        bstack1l1l11ll1ll_opy_.start()
        bstack1l1l11ll1ll_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡶࡴࡦࡽ࡮࠻ࠢࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࢀࠤࡴࡻࡴ࠾ࡽࡶࡩࡱ࡬࠮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡵࡷࡨࡴࡻࡴ࠯ࡴࡨࡥࡩ࠮ࠩࡾࠢࡨࡶࡷࡃࠢፊ") + str(self.process.stderr.read()) + bstack11l1l11_opy_ (u"ࠦࠧፋ"))
        if not self.bstack1l1l11lll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡡࠢፌ") + str(id(self)) + bstack11l1l11_opy_ (u"ࠨ࡝ࠡࡥ࡯ࡩࡦࡴࡵࡱࠤፍ"))
            self.__1l1l1l11ll1_opy_()
        self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡰࡳࡱࡦࡩࡸࡹ࡟ࡳࡧࡤࡨࡾࡀࠠࠣፎ") + str(self.bstack1l1l11lll11_opy_) + bstack11l1l11_opy_ (u"ࠣࠤፏ"))
        return self.bstack1l1l11lll11_opy_
    def __1l1l1l1l1ll_opy_(self, bstack1l1l1lll111_opy_=10):
        bstack1l11lll1l11_opy_ = time.time()
        while self.process and time.time() - bstack1l11lll1l11_opy_ < bstack1l1l1lll111_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11l1l11_opy_ (u"ࠤ࡬ࡨࡂࠨፐ") in line:
                    self.cli_bin_session_id = line.split(bstack11l1l11_opy_ (u"ࠥ࡭ࡩࡃࠢፑ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡨࡲࡩࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠼ࠥፒ") + str(self.cli_bin_session_id) + bstack11l1l11_opy_ (u"ࠧࠨፓ"))
                    continue
                if bstack11l1l11_opy_ (u"ࠨ࡬ࡪࡵࡷࡩࡳࡃࠢፔ") in line:
                    self.cli_listen_addr = line.split(bstack11l1l11_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣፕ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡥ࡯࡭ࡤࡲࡩࡴࡶࡨࡲࡤࡧࡤࡥࡴ࠽ࠦፖ") + str(self.cli_listen_addr) + bstack11l1l11_opy_ (u"ࠤࠥፗ"))
                    continue
                if bstack11l1l11_opy_ (u"ࠥࡴࡴࡸࡴ࠾ࠤፘ") in line:
                    port = line.split(bstack11l1l11_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥፙ"))[-1:][0].strip()
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡶ࡯ࡳࡶ࠽ࠦፚ") + str(port) + bstack11l1l11_opy_ (u"ࠨࠢ፛"))
                    continue
                if line.strip() == bstack1l1l1ll11l1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11l1l11_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡉࡐࡡࡖࡘࡗࡋࡁࡎࠤ፜"), bstack11l1l11_opy_ (u"ࠣ࠳ࠥ፝")) == bstack11l1l11_opy_ (u"ࠤ࠴ࠦ፞"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l11lll11_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳ࠼ࠣࠦ፟") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧ፠"))
        return False
    @measure(event_name=EVENTS.bstack1l11lll1111_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def __1l1l1l11ll1_opy_(self):
        if self.bstack1l1l11ll1l1_opy_:
            self.bstack1lll1l11111_opy_.stop()
            start = datetime.now()
            if self.bstack1l1ll111l11_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1lll1l1_opy_:
                    self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠧࡹࡴࡰࡲࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤ፡"), datetime.now() - start)
                else:
                    self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥ።"), datetime.now() - start)
            self.__1l1l1l11111_opy_()
            start = datetime.now()
            self.bstack1l1l11ll1l1_opy_.close()
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠢࡥ࡫ࡶࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤ፣"), datetime.now() - start)
            self.bstack1l1l11ll1l1_opy_ = None
        if self.process:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡵࡷࡳࡵࠨ፤"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠤ࡮࡭ࡱࡲ࡟ࡵ࡫ࡰࡩࠧ፥"), datetime.now() - start)
            self.process = None
            if self.bstack1l1l1llllll_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1lll1ll1ll_opy_()
                self.logger.info(
                    bstack11l1l11_opy_ (u"࡚ࠥ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠥ፦").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11l1l11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ፧")] = self.config_testhub.build_hashed_id
        self.bstack1l1l11lll11_opy_ = False
    def __1l1l1111l1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11l1l11_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ፨")] = selenium.__version__
            data.frameworks.append(bstack11l1l11_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ፩"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ፪")] = __version__
            data.frameworks.append(bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ፫"))
        except:
            pass
    def bstack1l1l1ll1l11_opy_(self, hub_url: str, platform_index: int, bstack11ll111l1l_opy_: Any):
        if self.bstack1llllll111l_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠣࡷࡪࡺࡵࡱࠢࡶࡩࡱ࡫࡮ࡪࡷࡰ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨ፬"))
            return
        try:
            bstack1l11lll1l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11l1l11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ፭")
            self.bstack1llllll111l_opy_ = bstack1llllll11l1_opy_(
                cli.config.get(bstack11l1l11_opy_ (u"ࠦ࡭ࡻࡢࡖࡴ࡯ࠦ፮"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1llllll11ll_opy_={bstack11l1l11_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡤࡵࡰࡵ࡫ࡲࡲࡸࡥࡦࡳࡱࡰࡣࡨࡧࡰࡴࠤ፯"): bstack11ll111l1l_opy_}
            )
            def bstack1l1l11111ll_opy_(self):
                return
            if self.config.get(bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠣ፰"), True):
                Service.start = bstack1l1l11111ll_opy_
                Service.stop = bstack1l1l11111ll_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.upload_attachment = staticmethod(bstack1111l1l111_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1l11111l_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ፱"), datetime.now() - bstack1l11lll1l_opy_)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࠢ፲") + str(e) + bstack11l1l11_opy_ (u"ࠤࠥ፳"))
    def bstack1l11lll1l1l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack11111ll1l1_opy_
            self.bstack1llllll111l_opy_ = bstack1lll1ll11l1_opy_(
                platform_index,
                framework_name=bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ፴"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠽ࠤࠧ፵") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨ፶"))
            pass
    def bstack1l11lllllll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡵࡨࡸࠥࡻࡰࠣ፷"))
            return
        if bstack11ll1ll11_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11l1l11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ፸"): pytest.__version__ }, [bstack11l1l11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧ፹")], self.bstack1lll1l11111_opy_, self.bstack1llll1ll11l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l11lll11l1_opy_({ bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤ፺"): pytest.__version__ }, [bstack11l1l11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ፻")], self.bstack1lll1l11111_opy_, self.bstack1llll1ll11l_opy_)
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡺࡶࡨࡷࡹࡀࠠࠣ፼") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨ፽"))
        self.bstack1l1l11l1111_opy_()
    def bstack1l1l11l1111_opy_(self):
        if not self.bstack1l1l11l1ll_opy_():
            return
        bstack11ll11l1l1_opy_ = None
        def bstack1l11lll11l_opy_(config, startdir):
            return bstack11l1l11_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦ፾").format(bstack11l1l11_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ፿"))
        def bstack1l1111111_opy_():
            return
        def bstack1ll1l1111l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11l1l11_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨᎀ"):
                return bstack11l1l11_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣᎁ")
            else:
                return bstack11ll11l1l1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack11ll11l1l1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1l11lll11l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1111111_opy_
            Config.getoption = bstack1ll1l1111l_opy_
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡶࡦ࡬ࠥࡶࡹࡵࡧࡶࡸࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡧࡱࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠽ࠤࠧᎂ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧᎃ"))
    def bstack1l1l1111ll1_opy_(self):
        bstack1ll11l11l1_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll11l11l1_opy_, dict):
            if cli.config_observability:
                bstack1ll11l11l1_opy_.update(
                    {bstack11l1l11_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧᎄ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࡠࡶࡲࡣࡼࡸࡡࡱࠤᎅ") in accessibility.get(bstack11l1l11_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᎆ"), {}):
                    bstack1l1l111ll1l_opy_ = accessibility.get(bstack11l1l11_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎇ"))
                    bstack1l1l111ll1l_opy_.update({ bstack11l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡘࡴ࡝ࡲࡢࡲࠥᎈ"): bstack1l1l111ll1l_opy_.pop(bstack11l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࡤࡺ࡯ࡠࡹࡵࡥࡵࠨᎉ")) })
                bstack1ll11l11l1_opy_.update({bstack11l1l11_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᎊ"): accessibility })
        return bstack1ll11l11l1_opy_
    @measure(event_name=EVENTS.bstack1l11lll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1l1ll111l11_opy_(self, bstack1l1l1l1l1l1_opy_: str = None, bstack1l1l1ll1111_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1llll1ll11l_opy_:
            return
        bstack1l11lll1l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l1l1l1_opy_:
            req.bstack1l1l1l1l1l1_opy_ = bstack1l1l1l1l1l1_opy_
        if bstack1l1l1ll1111_opy_:
            req.bstack1l1l1ll1111_opy_ = bstack1l1l1ll1111_opy_
        try:
            r = self.bstack1llll1ll11l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡹࡵࡰࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᎋ"), datetime.now() - bstack1l11lll1l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1l111llll_opy_(self, key: str, value: timedelta):
        tag = bstack11l1l11_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᎌ") if self.bstack1ll1l1l1l_opy_() else bstack11l1l11_opy_ (u"ࠢ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࠨᎍ")
        self.bstack1l1l11ll111_opy_[bstack11l1l11_opy_ (u"ࠣ࠼ࠥᎎ").join([tag + bstack11l1l11_opy_ (u"ࠤ࠰ࠦᎏ") + str(id(self)), key])] += value
    def bstack1lll1ll1ll_opy_(self):
        if not os.getenv(bstack11l1l11_opy_ (u"ࠥࡈࡊࡈࡕࡈࡡࡓࡉࡗࡌࠢ᎐"), bstack11l1l11_opy_ (u"ࠦ࠵ࠨ᎑")) == bstack11l1l11_opy_ (u"ࠧ࠷ࠢ᎒"):
            return
        bstack1l11ll1ll11_opy_ = dict()
        bstack1lll1lll111_opy_ = []
        if self.test_framework:
            bstack1lll1lll111_opy_.extend(list(self.test_framework.bstack1lll1lll111_opy_.values()))
        if self.bstack1llllll111l_opy_:
            bstack1lll1lll111_opy_.extend(list(self.bstack1llllll111l_opy_.bstack1lll1lll111_opy_.values()))
        for instance in bstack1lll1lll111_opy_:
            if not instance.platform_index in bstack1l11ll1ll11_opy_:
                bstack1l11ll1ll11_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l11ll1ll11_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1lll1111_opy_().items():
                report[k] += v
                report[k.split(bstack11l1l11_opy_ (u"ࠨ࠺ࠣ᎓"))[0]] += v
        bstack1l1l1l111ll_opy_ = sorted([(k, v) for k, v in self.bstack1l1l11ll111_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1l11l11_opy_ = 0
        for r in bstack1l1l1l111ll_opy_:
            bstack1l11llll1l1_opy_ = r[1].total_seconds()
            bstack1l1l1l11l11_opy_ += bstack1l11llll1l1_opy_
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࢀࡸ࡛࠱࡟ࢀࡁࠧ᎔") + str(bstack1l11llll1l1_opy_) + bstack11l1l11_opy_ (u"ࠣࠤ᎕"))
        self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࠰࠱ࠧ᎖"))
        bstack1l1l11l1lll_opy_ = []
        for platform_index, report in bstack1l11ll1ll11_opy_.items():
            bstack1l1l11l1lll_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l11l1lll_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1l1l1_opy_ = set()
        bstack1l1ll11lll1_opy_ = 0
        for r in bstack1l1l11l1lll_opy_:
            bstack1l11llll1l1_opy_ = r[2].total_seconds()
            bstack1l1ll11lll1_opy_ += bstack1l11llll1l1_opy_
            bstack1lll1l1l1_opy_.add(r[0])
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡸࡪࡹࡴ࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࡿࡷࡡ࠰࡞ࡿ࠽ࡿࡷࡡ࠱࡞ࡿࡀࠦ᎗") + str(bstack1l11llll1l1_opy_) + bstack11l1l11_opy_ (u"ࠦࠧ᎘"))
        if self.bstack1ll1l1l1l_opy_():
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࠳࠭ࠣ᎙"))
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵࡀࡿࡹࡵࡴࡢ࡮ࡢࡧࡱ࡯ࡽࠡࡶࡨࡷࡹࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ࠯ࡾࡷࡹࡸࠨࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠬࢁࡂࠨ᎚") + str(bstack1l1ll11lll1_opy_) + bstack11l1l11_opy_ (u"ࠢࠣ᎛"))
        else:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࠧ᎜") + str(bstack1l1l1l11l11_opy_) + bstack11l1l11_opy_ (u"ࠤࠥ᎝"))
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࠱࠲ࠨ᎞"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, bstack1l1l1ll1lll_opy_: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            bstack1l1l1ll1lll_opy_=bstack1l1l1ll1lll_opy_
        )
        if not self.bstack1llll1ll11l_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡨࡲࡩࡠࡵࡨࡶࡻ࡯ࡣࡦࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣ᎟"))
            return None
        response = self.bstack1llll1ll11l_opy_.TestOrchestration(request)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶ࠰ࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠰ࡷࡪࡹࡳࡪࡱࡱࡁࢀࢃࠢᎠ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1ll111111_opy_(self, r):
        if r is not None and getattr(r, bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࠧᎡ"), None) and getattr(r.testhub, bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧᎢ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11l1l11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᎣ")))
            for bstack1l1ll11ll11_opy_, err in errors.items():
                if err[bstack11l1l11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᎤ")] == bstack11l1l11_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᎥ"):
                    self.logger.info(err[bstack11l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᎦ")])
                else:
                    self.logger.error(err[bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ꭷ")])
    def bstack1llll1l11l_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()