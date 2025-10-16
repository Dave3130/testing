# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
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
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l111_opy_ import bstack1l1l1ll1111_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1ll111_opy_ import bstack1l1ll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1l1l11l1l1l_opy_ import bstack1l1l111l11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1lll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.bstack1l11lll1lll_opy_ import bstack1l1l1l1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll11111l_opy_ import bstack1ll11111l_opy_, Events, bstack111lll1l1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l11ll1ll_opy_ import bstack1l1l1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1lll11ll111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1lll1l1_opy_
from bstack_utils.helper import Notset, bstack1l1l11ll11l_opy_, get_cli_dir, bstack1l11lll11ll_opy_, bstack1llllll1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll111111l1_opy_ import bstack1ll11l11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1l1111l_opy_ import bstack1ll1lllll_opy_
from bstack_utils.helper import Notset, bstack1l1l11ll11l_opy_, get_cli_dir, bstack1l11lll11ll_opy_, bstack1llllll1l1_opy_, bstack111l1l11l1_opy_, bstack11l11111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll1l1111_opy_, bstack1llll1l11l1_opy_, bstack1ll11l1l11l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llllll11ll_opy_, bstack11111111ll_opy_, bstack1lllllll1ll_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1l1l11ll1l_opy_ import bstack111l11l111_opy_
from bstack_utils import bstack1l1l1ll111_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1lll11lll_opy_, bstack11llll111l_opy_
logger = bstack1l1l1ll111_opy_.get_logger(__name__, bstack1l1l1ll111_opy_.bstack1l1l1l1111l_opy_())
def bstack1l1l111lll1_opy_(bs_config):
    bstack1l1l1l11l1l_opy_ = None
    bstack1l1l111ll1l_opy_ = None
    try:
        bstack1l1l111ll1l_opy_ = get_cli_dir()
        bstack1l1l1l11l1l_opy_ = bstack1l11lll11ll_opy_(bstack1l1l111ll1l_opy_)
        bstack1l1l11ll111_opy_ = bstack1l1l11ll11l_opy_(bstack1l1l1l11l1l_opy_, bstack1l1l111ll1l_opy_, bs_config)
        bstack1l1l1l11l1l_opy_ = bstack1l1l11ll111_opy_ if bstack1l1l11ll111_opy_ else bstack1l1l1l11l1l_opy_
        if not bstack1l1l1l11l1l_opy_:
            raise ValueError(bstack1ll1ll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤዪ"))
    except Exception as ex:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡷ࡬ࡪࠦ࡬ࡢࡶࡨࡷࡹࠦࡢࡪࡰࡤࡶࡾࠦࡻࡾࠤያ").format(ex))
        bstack1l1l1l11l1l_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠥዬ"))
        if bstack1l1l1l11l1l_opy_:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡈࡤࡰࡱ࡯࡮ࡨࠢࡥࡥࡨࡱࠠࡵࡱࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠦࡦࡳࡱࡰࠤࡪࡴࡶࡪࡴࡲࡲࡲ࡫࡮ࡵ࠼ࠣࠦይ") + str(bstack1l1l1l11l1l_opy_) + bstack1ll1ll1_opy_ (u"ࠤࠥዮ"))
        else:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡒࡴࠦࡶࡢ࡮࡬ࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠼ࠢࡶࡩࡹࡻࡰࠡ࡯ࡤࡽࠥࡨࡥࠡ࡫ࡱࡧࡴࡳࡰ࡭ࡧࡷࡩ࠳ࠨዯ"))
    return bstack1l1l1l11l1l_opy_, bstack1l1l111ll1l_opy_
bstack1l1l1llll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠦ࠾࠿࠹࠺ࠤደ")
bstack1l11ll1lll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡸࡥࡢࡦࡼࠦዱ")
bstack1l1l11l11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥዲ")
bstack1l1l1l1ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡍࡋࡖࡘࡊࡔ࡟ࡂࡆࡇࡖࠧዳ")
bstack111l1ll1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠦዴ")
bstack1l1l11l1ll1_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡴࠥࠬࡄ࡯ࠩ࠯ࠬࠫࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡾࡅࡗ࠮࠴ࠪࠣድ"))
bstack1l1ll11111l_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡨࡪࡼࡥ࡭ࡱࡳࡱࡪࡴࡴࠣዶ")
bstack1l11lll1l11_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡔࡘࡃࡆࡡࡉࡅࡑࡒࡂࡂࡅࡎࠦዷ")
bstack1l1ll111l1l_opy_ = [
    Events.bstack11l111ll1l_opy_,
    Events.CONNECT,
    Events.bstack11l11l11ll_opy_,
]
class SDKCLI:
    _1ll1ll1lll1_opy_ = None
    process: Union[None, Any]
    bstack1l1ll11ll1l_opy_: bool
    bstack1l1l1111lll_opy_: bool
    bstack1l1ll11lll1_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l1l11l11_opy_: Union[None, grpc.Channel]
    bstack1l1l11lllll_opy_: str
    test_framework: TestFramework
    bstack1lllll1ll1l_opy_: bstack1lll11ll111_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l111l111_opy_: bstack1l1l1l1lll1_opy_
    accessibility: bstack1l1l1ll1111_opy_
    bstack11l1l1111l_opy_: bstack1ll1lllll_opy_
    ai: bstack1l1ll1l1111_opy_
    bstack1l11lll1l1l_opy_: bstack1l1l111l11l_opy_
    bstack1l1l111llll_opy_: List[bstack1llllllll11_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1l111ll_opy_: Any
    bstack1l1ll1111ll_opy_: Dict[str, timedelta]
    bstack1l11llllll1_opy_: str
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    def __new__(cls):
        if not cls._1ll1ll1lll1_opy_:
            cls._1ll1ll1lll1_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll1lll1_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1ll11ll1l_opy_ = False
        self.bstack1l1l1l11l11_opy_ = None
        self.bstack1lllll1lll1_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l1l1ll1l_opy_, None)
        self.bstack1l11llll111_opy_ = os.environ.get(bstack1l1l11l11l1_opy_, bstack1ll1ll1_opy_ (u"ࠧࠨዸ")) == bstack1ll1ll1_opy_ (u"ࠨࠢዹ")
        self.bstack1l1l1111lll_opy_ = False
        self.bstack1l1ll11lll1_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1l111ll_opy_ = None
        self.test_framework = None
        self.bstack1lllll1ll1l_opy_ = None
        self.bstack1l1l11lllll_opy_=bstack1ll1ll1_opy_ (u"ࠢࠣዺ")
        self.session_framework = None
        self.logger = bstack1l1l1ll111_opy_.get_logger(self.__class__.__name__, bstack1l1l1ll111_opy_.bstack1l1l1l1111l_opy_())
        self.bstack1l1ll1111ll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll1l11111_opy_ = bstack1lll11lllll_opy_()
        self.bstack1l1ll111ll1_opy_ = None
        self.bstack1ll1lll11ll_opy_ = None
        self.bstack1l1l111l111_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l111llll_opy_ = []
    def bstack11l1l111ll_opy_(self):
        return os.environ.get(bstack111l1ll1ll_opy_).lower().__eq__(bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡹࡪࠨዻ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l11lll1l11_opy_, bstack1ll1ll1_opy_ (u"ࠩࠪዼ")).lower() in [bstack1ll1ll1_opy_ (u"ࠪࡸࡷࡻࡥࠨዽ"), bstack1ll1ll1_opy_ (u"ࠫ࠶࠭ዾ"), bstack1ll1ll1_opy_ (u"ࠬࡿࡥࡴࠩዿ")]:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡆࡰࡴࡦ࡭ࡳ࡭ࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡰࡳࡩ࡫ࠠࡥࡷࡨࠤࡹࡵࠠࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡐࡔࡆࡉࡤࡌࡁࡍࡎࡅࡅࡈࡑࠠࡦࡰࡹ࡭ࡷࡵ࡮࡮ࡧࡱࡸࠥࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠢጀ"))
            os.environ[bstack1ll1ll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡉࡔࡡࡕ࡙ࡓࡔࡉࡏࡉࠥጁ")] = bstack1ll1ll1_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢጂ")
            return False
        if bstack1ll1ll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ጃ") in config and str(config[bstack1ll1ll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧጄ")]).lower() != bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪጅ"):
            return False
        bstack1l1l1lll1l1_opy_ = [bstack1ll1ll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧጆ"), bstack1ll1ll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥጇ")]
        bstack1l1l11111l1_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥገ")) in bstack1l1l1lll1l1_opy_ or os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩጉ")) in bstack1l1l1lll1l1_opy_
        os.environ[bstack1ll1ll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡋࡖࡣࡗ࡛ࡎࡏࡋࡑࡋࠧጊ")] = str(bstack1l1l11111l1_opy_) # bstack1l1l1ll11l1_opy_ bstack1l1l1llllll_opy_ VAR to bstack1l1l1ll1l11_opy_ is binary running
        return bstack1l1l11111l1_opy_
    def bstack11l111l1l_opy_(self):
        for event in bstack1l1ll111l1l_opy_:
            bstack1ll11111l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1ll11111l_opy_.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡿࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࡾࠢࡀࡂࠥࢁࡡࡳࡩࡶࢁࠥࠨጋ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠦࠧጌ"))
            )
        bstack1ll11111l_opy_.register(Events.bstack11l111ll1l_opy_, self.__1l1l1l11111_opy_)
        bstack1ll11111l_opy_.register(Events.CONNECT, self.__1l1l1lll11l_opy_)
        bstack1ll11111l_opy_.register(Events.bstack11l11l11ll_opy_, self.__1l1l11l11ll_opy_)
        bstack1ll11111l_opy_.register(Events.bstack11l11l1ll_opy_, self.__1l1l1l1l111_opy_)
    def bstack11111ll11l_opy_(self):
        return not self.bstack1l11llll111_opy_ and os.environ.get(bstack1l1l11l11l1_opy_, bstack1ll1ll1_opy_ (u"ࠧࠨግ")) != bstack1ll1ll1_opy_ (u"ࠨࠢጎ")
    def is_running(self):
        if self.bstack1l11llll111_opy_:
            return self.bstack1l1ll11ll1l_opy_
        else:
            return bool(self.bstack1l1l1l11l11_opy_)
    def bstack1l1l111l1ll_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l111llll_opy_) and cli.is_running()
    def __1l1l1ll1l1l_opy_(self, bstack1l1l11l111l_opy_=10):
        if self.bstack1lllll1lll1_opy_:
            return
        bstack111lllll1_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l1l1ll1l_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢ࡜ࠤጏ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠣ࡟ࠣࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡳ࡭ࠢጐ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1ll1ll1_opy_ (u"ࠤࡪࡶࡵࡩ࠮ࡦࡰࡤࡦࡱ࡫࡟ࡩࡶࡷࡴࡤࡶࡲࡰࡺࡼࠦ጑"), 0), (bstack1ll1ll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠯ࡧࡱࡥࡧࡲࡥࡠࡪࡷࡸࡵࡹ࡟ࡱࡴࡲࡼࡾࠨጒ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l11l111l_opy_)
        self.bstack1l1l1l11l11_opy_ = channel
        self.bstack1lllll1lll1_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l1l11l11_opy_)
        self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡦࡳࡳࡴࡥࡤࡶࠥጓ"), datetime.now() - bstack111lllll1_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l1l1ll1l_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪ࠺ࠡ࡫ࡶࡣࡨ࡮ࡩ࡭ࡦࡢࡴࡷࡵࡣࡦࡵࡶࡁࠧጔ") + str(self.bstack11111ll11l_opy_()) + bstack1ll1ll1_opy_ (u"ࠨࠢጕ"))
    def __1l1l11l11ll_opy_(self, event_name):
        if self.bstack11111ll11l_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡵࡷࡳࡵࡶࡩ࡯ࡩࠣࡇࡑࡏࠢ጖"))
        self.__1l1l1lllll1_opy_()
    def __1l1l1l1l111_opy_(self, event_name, bstack1l1l1l11lll_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠣࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠣ጗"))
        bstack1l11llll11l_opy_ = Path(bstack1lll1ll111l_opy_ (u"ࠤࡾࡷࡪࡲࡦ࠯ࡥ࡯࡭ࡤࡪࡩࡳࡿ࠲ࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࡷ࠳ࡰࡳࡰࡰࠥጘ"))
        if self.bstack1l1l111ll1l_opy_ and bstack1l11llll11l_opy_.exists():
            with open(bstack1l11llll11l_opy_, bstack1ll1ll1_opy_ (u"ࠪࡶࠬጙ"), encoding=bstack1ll1ll1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪጚ")) as fp:
                data = json.load(fp)
                try:
                    bstack111l1l11l1_opy_(bstack1ll1ll1_opy_ (u"ࠬࡖࡏࡔࡖࠪጛ"), bstack111l11l111_opy_(bstack1l1lll1lll_opy_), data, {
                        bstack1ll1ll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫጜ"): (self.config[bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩጝ")], self.config[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫጞ")])
                    })
                except Exception as e:
                    logger.debug(bstack11llll111l_opy_.format(str(e)))
            bstack1l11llll11l_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l1l1llll_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1l1l11111_opy_(self, event_name: str, data):
        from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
        self.bstack1l1l11lllll_opy_, self.bstack1l1l111ll1l_opy_ = bstack1l1l111lll1_opy_(data.bs_config)
        os.environ[bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠ࡙ࡕࡍ࡙ࡇࡂࡍࡇࡢࡈࡎࡘࠧጟ")] = self.bstack1l1l111ll1l_opy_
        if not self.bstack1l1l11lllll_opy_ or not self.bstack1l1l111ll1l_opy_:
            raise ValueError(bstack1ll1ll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡉࡌࡊࠢࡥ࡭ࡳࡧࡲࡺࠤጠ"))
        if self.bstack11111ll11l_opy_():
            self.__1l1l1lll11l_opy_(event_name, bstack111lll1l1_opy_())
            return
        try:
            bstack1lllll1l11l_opy_.end(EVENTS.bstack111l1l1111_opy_.value, EVENTS.bstack111l1l1111_opy_.value + bstack1ll1ll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦጡ"), EVENTS.bstack111l1l1111_opy_.value + bstack1ll1ll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥጢ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡃࡰ࡯ࡳࡰࡪࡺࡥࠡࡕࡇࡏ࡙ࠥࡥࡵࡷࡳ࠲ࠧጣ"))
        except Exception as e:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡽࢀࠦጤ").format(e))
        start = datetime.now()
        is_started = self.__1l1ll1111l1_opy_()
        self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡵࡳࡥࡼࡴ࡟ࡵ࡫ࡰࡩࠧጥ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l1ll1l1l_opy_()
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࡢࡸ࡮ࡳࡥࠣጦ"), datetime.now() - start)
            start = datetime.now()
            self.__1l1l11lll1l_opy_(data)
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡸ࡮ࡳࡥࠣጧ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l111111l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1l1lll11l_opy_(self, event_name: str, data: bstack111lll1l1_opy_):
        if not self.bstack11111ll11l_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱࡱࡲࡪࡩࡴ࠻ࠢࡱࡳࡹࠦࡡࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳࠣጨ"))
            return
        bin_session_id = os.environ.get(bstack1l1l11l11l1_opy_)
        start = datetime.now()
        self.__1l1l1ll1l1l_opy_()
        self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦጩ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠢࡷࡳࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠࡄࡎࡌࠤࠧጪ") + str(bin_session_id) + bstack1ll1ll1_opy_ (u"ࠢࠣጫ"))
        start = datetime.now()
        self.__1l1ll111lll_opy_()
        self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨጬ"), datetime.now() - start)
    def __1l1ll11l11l_opy_(self):
        if not self.bstack1lllll1lll1_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡦࡥࡳࡴ࡯ࡵࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡩࠥࡳ࡯ࡥࡷ࡯ࡩࡸࠨጭ"))
            return
        bstack1l1ll11ll11_opy_ = {
            bstack1ll1ll1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢጮ"): (bstack1ll1lll1ll1_opy_, bstack1llll11ll11_opy_, bstack1lll1lll1l1_opy_),
            bstack1ll1ll1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨጯ"): (bstack1llll1llll1_opy_, bstack1lll11llll1_opy_, bstack111111111l_opy_),
        }
        if not self.bstack1l1ll111ll1_opy_ and self.session_framework in bstack1l1ll11ll11_opy_:
            bstack1l11lll1111_opy_, bstack1l11lllllll_opy_, bstack1l1ll11l111_opy_ = bstack1l1ll11ll11_opy_[self.session_framework]
            bstack1l1l1ll1lll_opy_ = bstack1l11lllllll_opy_()
            self.bstack1ll1lll11ll_opy_ = bstack1l1l1ll1lll_opy_
            self.bstack1l1ll111ll1_opy_ = bstack1l1ll11l111_opy_
            self.bstack1l1l111llll_opy_.append(bstack1l1l1ll1lll_opy_)
            self.bstack1l1l111llll_opy_.append(bstack1l11lll1111_opy_(self.bstack1ll1lll11ll_opy_))
        if not self.bstack1l1l111l111_opy_ and self.config_observability and self.config_observability.success: # bstack1lllll111l1_opy_
            self.bstack1l1l111l111_opy_ = bstack1l1l1l1lll1_opy_(self.bstack1l1ll111ll1_opy_, self.bstack1ll1lll11ll_opy_) # bstack1l1l1ll111l_opy_
            self.bstack1l1l111llll_opy_.append(self.bstack1l1l111l111_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l1ll1111_opy_(self.bstack1l1ll111ll1_opy_, self.bstack1ll1lll11ll_opy_)
            self.bstack1l1l111llll_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1ll1ll1_opy_ (u"ࠧࡹࡥ࡭ࡨࡋࡩࡦࡲࠢጰ"), False) == True:
            self.ai = bstack1l1ll1l1111_opy_()
            self.bstack1l1l111llll_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1l111ll_opy_ and self.bstack1l1l1l111ll_opy_.success:
            self.percy = bstack1l1l111l11l_opy_(self.bstack1l1l1l111ll_opy_)
            self.bstack1l1l111llll_opy_.append(self.percy)
        for mod in self.bstack1l1l111llll_opy_:
            if not mod.bstack1lll1l1111l_opy_():
                mod.configure(self.bstack1lllll1lll1_opy_, self.config, self.cli_bin_session_id, self.bstack1lll1l11111_opy_)
    def __1l1l11111ll_opy_(self):
        for mod in self.bstack1l1l111llll_opy_:
            if mod.bstack1lll1l1111l_opy_():
                mod.configure(self.bstack1lllll1lll1_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11lll111l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1l11lll1l_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1l1111lll_opy_:
            return
        self.__1l1l1111l1l_opy_(data)
        bstack111lllll1_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1ll1ll1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨጱ")
        req.sdk_language = bstack1ll1ll1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢጲ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1l11l1ll1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣ࡝ࠥጳ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠤࡠࠤࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡸࡺࡡࡳࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣጴ"))
            r = self.bstack1lllll1lll1_opy_.StartBinSession(req)
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡷࡥࡷࡺ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧጵ"), datetime.now() - bstack111lllll1_opy_)
            os.environ[bstack1l1l11l11l1_opy_] = r.bin_session_id
            self.__1l1l11l1lll_opy_(r)
            self.__1l1ll11l11l_opy_()
            self.bstack1lll1l11111_opy_.start()
            self.bstack1l1l1111lll_opy_ = True
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡠࠨጶ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠧࡣࠠ࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡦࡦࠥጷ"))
        except grpc.bstack1l1l1l1l1ll_opy_ as bstack1l1l111ll11_opy_:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡺࡩ࡮ࡧࡲࡩࡺࡺ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጸ") + str(bstack1l1l111ll11_opy_) + bstack1ll1ll1_opy_ (u"ࠢࠣጹ"))
            traceback.print_exc()
            raise bstack1l1l111ll11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧጺ") + str(e) + bstack1ll1ll1_opy_ (u"ࠤࠥጻ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l11l1l11_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1ll111lll_opy_(self):
        if not self.bstack11111ll11l_opy_() or not self.cli_bin_session_id or self.bstack1l1ll11lll1_opy_:
            return
        bstack111lllll1_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪጼ"), bstack1ll1ll1_opy_ (u"ࠫ࠵࠭ጽ")))
        try:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡡࠢጾ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠨ࡝ࠡࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡦࡳࡳࡴࡥࡤࡶࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣጿ"))
            r = self.bstack1lllll1lll1_opy_.ConnectBinSession(req)
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡩ࡯࡯ࡰࡨࡧࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦፀ"), datetime.now() - bstack111lllll1_opy_)
            self.__1l1l11l1lll_opy_(r)
            self.__1l1ll11l11l_opy_()
            self.bstack1lll1l11111_opy_.start()
            self.bstack1l1ll11lll1_opy_ = True
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣ࡝ࠥፁ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠤࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠣፂ"))
        except grpc.bstack1l1l1l1l1ll_opy_ as bstack1l1l111ll11_opy_:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡷ࡭ࡲ࡫࡯ࡦࡷࡷ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧፃ") + str(bstack1l1l111ll11_opy_) + bstack1ll1ll1_opy_ (u"ࠦࠧፄ"))
            traceback.print_exc()
            raise bstack1l1l111ll11_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤፅ") + str(e) + bstack1ll1ll1_opy_ (u"ࠨࠢፆ"))
            traceback.print_exc()
            raise e
    def __1l1l11l1lll_opy_(self, r):
        self.bstack1l1l1111ll1_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1ll1ll1_opy_ (u"ࠢࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡸ࡫ࡲࡷࡧࡵࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨፇ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1ll1ll1_opy_ (u"ࠣࡧࡰࡴࡹࡿࠠࡤࡱࡱࡪ࡮࡭ࠠࡧࡱࡸࡲࡩࠨፈ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1ll1ll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡦࡴࡦࡽࠥ࡯ࡳࠡࡵࡨࡲࡹࠦ࡯࡯࡮ࡼࠤࡦࡹࠠࡱࡣࡵࡸࠥࡵࡦࠡࡶ࡫ࡩࠥࠨࡃࡰࡰࡱࡩࡨࡺࡂࡪࡰࡖࡩࡸࡹࡩࡰࡰ࠯ࠦࠥࡧ࡮ࡥࠢࡷ࡬࡮ࡹࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢ࡬ࡷࠥࡧ࡬ࡴࡱࠣࡹࡸ࡫ࡤࠡࡤࡼࠤࡘࡺࡡࡳࡶࡅ࡭ࡳ࡙ࡥࡴࡵ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࡷ࡫ࡦࡰࡴࡨ࠰ࠥࡔ࡯࡯ࡧࠣ࡬ࡦࡴࡤ࡭࡫ࡱ࡫ࠥ࡯ࡳࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦፉ")
        self.bstack1l1l1l111ll_opy_ = getattr(r, bstack1ll1ll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩፊ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨፋ")] = self.config_testhub.jwt
        os.environ[bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪፌ")] = self.config_testhub.build_hashed_id
    def bstack1l1l1l111l1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1ll11ll1l_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l11lll11l1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l11lll11l1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1l1l111l1_opy_(event_name=EVENTS.bstack1l1l1111111_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1ll1111l1_opy_(self, bstack1l1l11l111l_opy_=10):
        if self.bstack1l1ll11ll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡳࡵࡣࡵࡸ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡳࡷࡱࡲ࡮ࡴࡧࠣፍ"))
            return True
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨፎ"))
        if os.getenv(bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡊࡔࡖࠣፏ")) == bstack1l1ll11111l_opy_:
            self.cli_bin_session_id = bstack1l1ll11111l_opy_
            self.cli_listen_addr = bstack1ll1ll1_opy_ (u"ࠤࡸࡲ࡮ࡾ࠺࠰ࡶࡰࡴ࠴ࡹࡤ࡬࠯ࡳࡰࡦࡺࡦࡰࡴࡰ࠱ࠪࡹ࠮ࡴࡱࡦ࡯ࠧፐ") % (self.cli_bin_session_id)
            self.bstack1l1ll11ll1l_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l11lllll_opy_, bstack1ll1ll1_opy_ (u"ࠥࡷࡩࡱࠢፑ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1ll1ll1_opy_ compat for text=True in bstack1l1l1lll1ll_opy_ python
            encoding=bstack1ll1ll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥፒ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l1l11ll1l1_opy_ = threading.Thread(target=self.__1l1ll11l1ll_opy_, args=(bstack1l1l11l111l_opy_,))
        bstack1l1l11ll1l1_opy_.start()
        bstack1l1l11ll1l1_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡸࡶࡡࡸࡰ࠽ࠤࡷ࡫ࡴࡶࡴࡱࡧࡴࡪࡥ࠾ࡽࡶࡩࡱ࡬࠮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡴࡨࡸࡺࡸ࡮ࡤࡱࡧࡩࢂࠦ࡯ࡶࡶࡀࡿࡸ࡫࡬ࡧ࠰ࡳࡶࡴࡩࡥࡴࡵ࠱ࡷࡹࡪ࡯ࡶࡶ࠱ࡶࡪࡧࡤࠩࠫࢀࠤࡪࡸࡲ࠾ࠤፓ") + str(self.process.stderr.read()) + bstack1ll1ll1_opy_ (u"ࠨࠢፔ"))
        if not self.bstack1l1ll11ll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢ࡜ࠤፕ") + str(id(self)) + bstack1ll1ll1_opy_ (u"ࠣ࡟ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠦፖ"))
            self.__1l1l1lllll1_opy_()
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡲࡵࡳࡨ࡫ࡳࡴࡡࡵࡩࡦࡪࡹ࠻ࠢࠥፗ") + str(self.bstack1l1ll11ll1l_opy_) + bstack1ll1ll1_opy_ (u"ࠥࠦፘ"))
        return self.bstack1l1ll11ll1l_opy_
    def __1l1ll11l1ll_opy_(self, bstack1l1l11l1111_opy_=10):
        bstack1l11lll1ll1_opy_ = time.time()
        while self.process and time.time() - bstack1l11lll1ll1_opy_ < bstack1l1l11l1111_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1ll1ll1_opy_ (u"ࠦ࡮ࡪ࠽ࠣፙ") in line:
                    self.cli_bin_session_id = line.split(bstack1ll1ll1_opy_ (u"ࠧ࡯ࡤ࠾ࠤፚ"))[-1:][0].strip()
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡣ࡭࡫ࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧ࠾ࠧ፛") + str(self.cli_bin_session_id) + bstack1ll1ll1_opy_ (u"ࠢࠣ፜"))
                    continue
                if bstack1ll1ll1_opy_ (u"ࠣ࡮࡬ࡷࡹ࡫࡮࠾ࠤ፝") in line:
                    self.cli_listen_addr = line.split(bstack1ll1ll1_opy_ (u"ࠤ࡯࡭ࡸࡺࡥ࡯࠿ࠥ፞"))[-1:][0].strip()
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡧࡱ࡯࡟࡭࡫ࡶࡸࡪࡴ࡟ࡢࡦࡧࡶ࠿ࠨ፟") + str(self.cli_listen_addr) + bstack1ll1ll1_opy_ (u"ࠦࠧ፠"))
                    continue
                if bstack1ll1ll1_opy_ (u"ࠧࡶ࡯ࡳࡶࡀࠦ፡") in line:
                    port = line.split(bstack1ll1ll1_opy_ (u"ࠨࡰࡰࡴࡷࡁࠧ።"))[-1:][0].strip()
                    self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡱࡱࡵࡸ࠿ࠨ፣") + str(port) + bstack1ll1ll1_opy_ (u"ࠣࠤ፤"))
                    continue
                if line.strip() == bstack1l11ll1lll1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1ll1ll1_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡋࡒࡣࡘ࡚ࡒࡆࡃࡐࠦ፥"), bstack1ll1ll1_opy_ (u"ࠥ࠵ࠧ፦")) == bstack1ll1ll1_opy_ (u"ࠦ࠶ࠨ፧"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1ll11ll1l_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵ࠾ࠥࠨ፨") + str(e) + bstack1ll1ll1_opy_ (u"ࠨࠢ፩"))
        return False
    @measure(event_name=EVENTS.bstack1l1ll11llll_opy_, stage=STAGE.bstack111l1l111_opy_)
    def __1l1l1lllll1_opy_(self):
        if self.bstack1l1l1l11l11_opy_:
            self.bstack1lll1l11111_opy_.stop()
            start = datetime.now()
            if self.bstack1l1l1lll111_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1ll11lll1_opy_:
                    self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠢࡴࡶࡲࡴࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦ፪"), datetime.now() - start)
                else:
                    self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡵࡷࡳࡵࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧ፫"), datetime.now() - start)
            self.__1l1l11111ll_opy_()
            start = datetime.now()
            self.bstack1l1l1l11l11_opy_.close()
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠤࡧ࡭ࡸࡩ࡯࡯ࡰࡨࡧࡹࡥࡴࡪ࡯ࡨࠦ፬"), datetime.now() - start)
            self.bstack1l1l1l11l11_opy_ = None
        if self.process:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡷࡹࡵࡰࠣ፭"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠦࡰ࡯࡬࡭ࡡࡷ࡭ࡲ࡫ࠢ፮"), datetime.now() - start)
            self.process = None
            if self.bstack1l11llll111_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11ll11lll_opy_()
                self.logger.info(
                    bstack1ll1ll1_opy_ (u"ࠧ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠧ፯").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ፰")] = self.config_testhub.build_hashed_id
        self.bstack1l1ll11ll1l_opy_ = False
    def __1l1l1111l1l_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1ll1ll1_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ፱")] = selenium.__version__
            data.frameworks.append(bstack1ll1ll1_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ፲"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1ll1ll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ፳")] = __version__
            data.frameworks.append(bstack1ll1ll1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ፴"))
        except:
            pass
    def bstack1l11lllll1l_opy_(self, hub_url: str, platform_index: int, bstack1l1l1l1l1l_opy_: Any):
        if self.bstack1lllll1ll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡵࡨࡸࠥࡻࡰࠣ፵"))
            return
        try:
            bstack111lllll1_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1ll1ll1_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ፶")
            self.bstack1lllll1ll1l_opy_ = bstack111111111l_opy_(
                cli.config.get(bstack1ll1ll1_opy_ (u"ࠨࡨࡶࡤࡘࡶࡱࠨ፷"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lllll11l11_opy_={bstack1ll1ll1_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦ፸"): bstack1l1l1l1l1l_opy_}
            )
            def bstack1l1l1llll11_opy_(self):
                return
            if self.config.get(bstack1ll1ll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠥ፹"), True):
                Service.start = bstack1l1l1llll11_opy_
                Service.stop = bstack1l1l1llll11_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1ll1lllll_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11l11ll1_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ፺"), datetime.now() - bstack111lllll1_opy_)
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠺ࠡࠤ፻") + str(e) + bstack1ll1ll1_opy_ (u"ࠦࠧ፼"))
    def bstack1l1l11llll1_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1l11l11l1l_opy_
            self.bstack1lllll1ll1l_opy_ = bstack1lll1lll1l1_opy_(
                platform_index,
                framework_name=bstack1ll1ll1_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ፽"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠿ࠦࠢ፾") + str(e) + bstack1ll1ll1_opy_ (u"ࠢࠣ፿"))
            pass
    def bstack1l1l1l1l11l_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠢࡶࡩࡹࡻࡰࠡࡲࡼࡸࡪࡹࡴ࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡷࡪࡺࠠࡶࡲࠥᎀ"))
            return
        if bstack1llllll1l1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1ll1ll1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤᎁ"): pytest.__version__ }, [bstack1ll1ll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᎂ")], self.bstack1lll1l11111_opy_, self.bstack1lllll1lll1_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l1l1l1l1_opy_({ bstack1ll1ll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᎃ"): pytest.__version__ }, [bstack1ll1ll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧᎄ")], self.bstack1lll1l11111_opy_, self.bstack1lllll1lll1_opy_)
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡼࡸࡪࡹࡴ࠻ࠢࠥᎅ") + str(e) + bstack1ll1ll1_opy_ (u"ࠢࠣᎆ"))
        self.bstack1l11llll1ll_opy_()
    def bstack1l11llll1ll_opy_(self):
        if not self.bstack11l1l111ll_opy_():
            return
        bstack1ll1ll11l1_opy_ = None
        def bstack11111lll1_opy_(config, startdir):
            return bstack1ll1ll1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨᎇ").format(bstack1ll1ll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣᎈ"))
        def bstack1ll11ll1l_opy_():
            return
        def bstack1l1lll1l1l_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1ll1ll1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪᎉ"):
                return bstack1ll1ll1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥᎊ")
            else:
                return bstack1ll1ll11l1_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1ll1ll11l1_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack11111lll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll11ll1l_opy_
            Config.getoption = bstack1l1lll1l1l_opy_
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡸࡨ࡮ࠠࡱࡻࡷࡩࡸࡺࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡩࡳࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠿ࠦࠢᎋ") + str(e) + bstack1ll1ll1_opy_ (u"ࠨࠢᎌ"))
    def bstack1l1ll111l11_opy_(self):
        bstack1l11l1l1ll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1l11l1l1ll_opy_, dict):
            if cli.config_observability:
                bstack1l11l1l1ll_opy_.update(
                    {bstack1ll1ll1_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢᎍ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡢࡸࡴࡥࡷࡳࡣࡳࠦᎎ") in accessibility.get(bstack1ll1ll1_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᎏ"), {}):
                    bstack1l1l1ll11ll_opy_ = accessibility.get(bstack1ll1ll1_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦ᎐"))
                    bstack1l1l1ll11ll_opy_.update({ bstack1ll1ll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸ࡚࡯ࡘࡴࡤࡴࠧ᎑"): bstack1l1l1ll11ll_opy_.pop(bstack1ll1ll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹ࡟ࡵࡱࡢࡻࡷࡧࡰࠣ᎒")) })
                bstack1l11l1l1ll_opy_.update({bstack1ll1ll1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨ᎓"): accessibility })
        return bstack1l11l1l1ll_opy_
    @measure(event_name=EVENTS.bstack1l11llll1l1_opy_, stage=STAGE.bstack111l1l111_opy_)
    def bstack1l1l1lll111_opy_(self, bstack1l1l11lll11_opy_: str = None, bstack1l1ll111111_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1lllll1lll1_opy_:
            return
        bstack111lllll1_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l11lll11_opy_:
            req.bstack1l1l11lll11_opy_ = bstack1l1l11lll11_opy_
        if bstack1l1ll111111_opy_:
            req.bstack1l1ll111111_opy_ = bstack1l1ll111111_opy_
        try:
            r = self.bstack1lllll1lll1_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡴࡰࡲࡢࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣ᎔"), datetime.now() - bstack111lllll1_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1llll1ll11_opy_(self, key: str, value: timedelta):
        tag = bstack1ll1ll1_opy_ (u"ࠣࡥ࡫࡭ࡱࡪ࠭ࡱࡴࡲࡧࡪࡹࡳࠣ᎕") if self.bstack11111ll11l_opy_() else bstack1ll1ll1_opy_ (u"ࠤࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳࠣ᎖")
        self.bstack1l1ll1111ll_opy_[bstack1ll1ll1_opy_ (u"ࠥ࠾ࠧ᎗").join([tag + bstack1ll1ll1_opy_ (u"ࠦ࠲ࠨ᎘") + str(id(self)), key])] += value
    def bstack11ll11lll_opy_(self):
        if not os.getenv(bstack1ll1ll1_opy_ (u"ࠧࡊࡅࡃࡗࡊࡣࡕࡋࡒࡇࠤ᎙"), bstack1ll1ll1_opy_ (u"ࠨ࠰ࠣ᎚")) == bstack1ll1ll1_opy_ (u"ࠢ࠲ࠤ᎛"):
            return
        bstack1l1l1111l11_opy_ = dict()
        bstack1lll1l1ll1l_opy_ = []
        if self.test_framework:
            bstack1lll1l1ll1l_opy_.extend(list(self.test_framework.bstack1lll1l1ll1l_opy_.values()))
        if self.bstack1lllll1ll1l_opy_:
            bstack1lll1l1ll1l_opy_.extend(list(self.bstack1lllll1ll1l_opy_.bstack1lll1l1ll1l_opy_.values()))
        for instance in bstack1lll1l1ll1l_opy_:
            if not instance.platform_index in bstack1l1l1111l11_opy_:
                bstack1l1l1111l11_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l1111l11_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1lll11l1_opy_().items():
                report[k] += v
                report[k.split(bstack1ll1ll1_opy_ (u"ࠣ࠼ࠥ᎜"))[0]] += v
        bstack1l11lllll11_opy_ = sorted([(k, v) for k, v in self.bstack1l1ll1111ll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1l1ll11_opy_ = 0
        for r in bstack1l11lllll11_opy_:
            bstack1l1ll11l1l1_opy_ = r[1].total_seconds()
            bstack1l1l1l1ll11_opy_ += bstack1l1ll11l1l1_opy_
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀࡻࡳ࡝࠳ࡡࢂࡃࠢ᎝") + str(bstack1l1ll11l1l1_opy_) + bstack1ll1ll1_opy_ (u"ࠥࠦ᎞"))
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦ࠲࠳ࠢ᎟"))
        bstack1l1l1l11ll1_opy_ = []
        for platform_index, report in bstack1l1l1111l11_opy_.items():
            bstack1l1l1l11ll1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l1l1l11ll1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1l11l_opy_ = set()
        bstack1l1l111l1l1_opy_ = 0
        for r in bstack1l1l1l11ll1_opy_:
            bstack1l1ll11l1l1_opy_ = r[2].total_seconds()
            bstack1l1l111l1l1_opy_ += bstack1l1ll11l1l1_opy_
            bstack1lll1l11l_opy_.add(r[0])
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡺࡥࡴࡶ࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࠲ࢁࡲ࡜࠲ࡠࢁ࠿ࢁࡲ࡜࠳ࡠࢁࡂࠨᎠ") + str(bstack1l1ll11l1l1_opy_) + bstack1ll1ll1_opy_ (u"ࠨࠢᎡ"))
        if self.bstack11111ll11l_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢ࠮࠯ࠥᎢ"))
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࢁࡴࡰࡶࡤࡰࡤࡩ࡬ࡪࡿࠣࡸࡪࡹࡴ࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠱ࢀࡹࡴࡳࠪࡳࡰࡦࡺࡦࡰࡴࡰࡷ࠮ࢃ࠽ࠣᎣ") + str(bstack1l1l111l1l1_opy_) + bstack1ll1ll1_opy_ (u"ࠤࠥᎤ"))
        else:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥ࡟ࡵ࡫ࡲࡧ࡟ࠣࡧࡱ࡯࠺࡮ࡣ࡬ࡲ࠲ࡶࡲࡰࡥࡨࡷࡸࡃࠢᎥ") + str(bstack1l1l1l1ll11_opy_) + bstack1ll1ll1_opy_ (u"ࠦࠧᎦ"))
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧ࠳࠭ࠣᎧ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1lllll1lll1_opy_:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠨࡣ࡭࡫ࡢࡷࡪࡸࡶࡪࡥࡨࠤ࡮ࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࡥ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡪࡸࡦࡰࡴࡰࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥᎨ"))
            return None
        response = self.bstack1lllll1lll1_opy_.TestOrchestration(request)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸ࠲ࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠲ࡹࡥࡴࡵ࡬ࡳࡳࡃࡻࡾࠤᎩ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1l1111ll1_opy_(self, r):
        if r is not None and getattr(r, bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࠩᎪ"), None) and getattr(r.testhub, bstack1ll1ll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩᎫ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1ll1ll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᎬ")))
            for bstack1l11ll1llll_opy_, err in errors.items():
                if err[bstack1ll1ll1_opy_ (u"ࠫࡹࡿࡰࡦࠩᎭ")] == bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪᎮ"):
                    self.logger.info(err[bstack1ll1ll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᎯ")])
                else:
                    self.logger.error(err[bstack1ll1ll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᎰ")])
    def bstack11l1ll1ll_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()