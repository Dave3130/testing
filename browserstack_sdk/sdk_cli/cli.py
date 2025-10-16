# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1l1l1llll1l_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll1ll111_opy_ import bstack1l1ll1ll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll111111_opy_ import bstack1l11lll1111_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll1l1_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll11l_opy_ import bstack1ll1llll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll1ll_opy_ import bstack1llll1l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1l1l1111l11_opy_ import bstack1l1l11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1l1ll11ll_opy_ import bstack1l1ll11ll_opy_, Events, bstack1ll11l11l1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1l1l1ll1lll_opy_ import bstack1l1l1l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1lll11ll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l1l_opy_ import bstack1lll1l1ll11_opy_
from bstack_utils.helper import Notset, bstack1l11lll1l1l_opy_, get_cli_dir, bstack1l1l111l1ll_opy_, bstack1ll11llll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll11llll11_opy_ import bstack1ll11l11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1l111ll_opy_ import bstack1l1lll1lll_opy_
from bstack_utils.helper import Notset, bstack1l11lll1l1l_opy_, get_cli_dir, bstack1l1l111l1ll_opy_, bstack1ll11llll1_opy_, bstack1l1111111_opy_, bstack11l1l1lll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1l11l11_opy_, bstack1llll1l11l1_opy_, bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1111111l11_opy_, bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_
from bstack_utils.constants import *
from bstack_utils.bstack11111ll1l_opy_ import bstack1lll1ll11l_opy_
from bstack_utils import bstack1ll11111l1_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111l1lll11_opy_, bstack111llll1l_opy_
logger = bstack1ll11111l1_opy_.get_logger(__name__, bstack1ll11111l1_opy_.bstack1l1l111l111_opy_())
def bstack1l1l1lll1l1_opy_(bs_config):
    bstack1l1ll111lll_opy_ = None
    bstack1l1l1l11lll_opy_ = None
    try:
        bstack1l1l1l11lll_opy_ = get_cli_dir()
        bstack1l1ll111lll_opy_ = bstack1l1l111l1ll_opy_(bstack1l1l1l11lll_opy_)
        bstack1l1l11ll111_opy_ = bstack1l11lll1l1l_opy_(bstack1l1ll111lll_opy_, bstack1l1l1l11lll_opy_, bs_config)
        bstack1l1ll111lll_opy_ = bstack1l1l11ll111_opy_ if bstack1l1l11ll111_opy_ else bstack1l1ll111lll_opy_
        if not bstack1l1ll111lll_opy_:
            raise ValueError(bstack1lllll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣዩ"))
    except Exception as ex:
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡲࡡࡵࡧࡶࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࢁࡽࠣዪ").format(ex))
        bstack1l1ll111lll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤያ"))
        if bstack1l1ll111lll_opy_:
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬ࡲࡰ࡯ࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠻ࠢࠥዬ") + str(bstack1l1ll111lll_opy_) + bstack1lllll1_opy_ (u"ࠣࠤይ"))
        else:
            logger.debug(bstack1lllll1_opy_ (u"ࠤࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠻ࠡࡵࡨࡸࡺࡶࠠ࡮ࡣࡼࠤࡧ࡫ࠠࡪࡰࡦࡳࡲࡶ࡬ࡦࡶࡨ࠲ࠧዮ"))
    return bstack1l1ll111lll_opy_, bstack1l1l1l11lll_opy_
bstack1l11ll1llll_opy_ = bstack1lllll1_opy_ (u"ࠥ࠽࠾࠿࠹ࠣዯ")
bstack1l1ll11111l_opy_ = bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡡࡥࡻࠥደ")
bstack1l11lll1l11_opy_ = bstack1lllll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤዱ")
bstack1l1l11111ll_opy_ = bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡌࡊࡕࡗࡉࡓࡥࡁࡅࡆࡕࠦዲ")
bstack1l11ll111_opy_ = bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥዳ")
bstack1l1ll1111ll_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡳࠤࠫࡃ࡮࠯࠮ࠫࠪࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡽࡄࡖ࠭࠳࠰ࠢዴ"))
bstack1l1l1ll1l11_opy_ = bstack1lllll1_opy_ (u"ࠤࡧࡩࡻ࡫࡬ࡰࡲࡰࡩࡳࡺࠢድ")
bstack1l1l1l1llll_opy_ = bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡓࡗࡉࡅࡠࡈࡄࡐࡑࡈࡁࡄࡍࠥዶ")
bstack1l1l111l1l1_opy_ = [
    Events.bstack1lll11l111_opy_,
    Events.CONNECT,
    Events.bstack1ll11lllll_opy_,
]
class SDKCLI:
    _1ll1ll11lll_opy_ = None
    process: Union[None, Any]
    bstack1l1l1111lll_opy_: bool
    bstack1l1ll11llll_opy_: bool
    bstack1l1l1ll11l1_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1l1l111111l_opy_: Union[None, grpc.Channel]
    bstack1l1l1ll1ll1_opy_: str
    test_framework: TestFramework
    bstack1llll1l1lll_opy_: bstack1lll11ll1l1_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1l1l111ll11_opy_: bstack1l1l11llll1_opy_
    accessibility: bstack1l1l1llll1l_opy_
    bstack1ll1l111ll_opy_: bstack1l1lll1lll_opy_
    ai: bstack1l1ll1ll1l1_opy_
    bstack1l1ll11l1ll_opy_: bstack1l11lll1111_opy_
    bstack1l1l1l1l11l_opy_: List[bstack1llll1ll11l_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1l1l1lll111_opy_: Any
    bstack1l1l1l11l11_opy_: Dict[str, timedelta]
    bstack1l1ll11l1l1_opy_: str
    bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_
    def __new__(cls):
        if not cls._1ll1ll11lll_opy_:
            cls._1ll1ll11lll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1ll11lll_opy_
    def __init__(self):
        self.process = None
        self.bstack1l1l1111lll_opy_ = False
        self.bstack1l1l111111l_opy_ = None
        self.bstack1111111l1l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1l1l11111ll_opy_, None)
        self.bstack1l11llll1l1_opy_ = os.environ.get(bstack1l11lll1l11_opy_, bstack1lllll1_opy_ (u"ࠦࠧዷ")) == bstack1lllll1_opy_ (u"ࠧࠨዸ")
        self.bstack1l1ll11llll_opy_ = False
        self.bstack1l1l1ll11l1_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1l1l1lll111_opy_ = None
        self.test_framework = None
        self.bstack1llll1l1lll_opy_ = None
        self.bstack1l1l1ll1ll1_opy_=bstack1lllll1_opy_ (u"ࠨࠢዹ")
        self.session_framework = None
        self.logger = bstack1ll11111l1_opy_.get_logger(self.__class__.__name__, bstack1ll11111l1_opy_.bstack1l1l111l111_opy_())
        self.bstack1l1l1l11l11_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack1lll11lllll_opy_ = bstack1lll1l1111l_opy_()
        self.bstack1l1l1l111ll_opy_ = None
        self.bstack1ll1lll1ll1_opy_ = None
        self.bstack1l1l111ll11_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1l1l1l1l11l_opy_ = []
    def bstack11ll11111_opy_(self):
        return os.environ.get(bstack1l11ll111_opy_).lower().__eq__(bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧዺ"))
    def is_enabled(self, config):
        if os.environ.get(bstack1l1l1l1llll_opy_, bstack1lllll1_opy_ (u"ࠨࠩዻ")).lower() in [bstack1lllll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧዼ"), bstack1lllll1_opy_ (u"ࠪ࠵ࠬዽ"), bstack1lllll1_opy_ (u"ࠫࡾ࡫ࡳࠨዾ")]:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡌ࡯ࡳࡥ࡬ࡲ࡬ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡ࡯ࡲࡨࡪࠦࡤࡶࡧࠣࡸࡴࠦࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡏࡓࡅࡈࡣࡋࡇࡌࡍࡄࡄࡇࡐࠦࡥ࡯ࡸ࡬ࡶࡴࡴ࡭ࡦࡰࡷࠤࡻࡧࡲࡪࡣࡥࡰࡪࠨዿ"))
            os.environ[bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤጀ")] = bstack1lllll1_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨጁ")
            return False
        if bstack1lllll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬጂ") in config and str(config[bstack1lllll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ጃ")]).lower() != bstack1lllll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩጄ"):
            return False
        bstack1l11lll11ll_opy_ = [bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦጅ"), bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤጆ")]
        bstack1l1l111l11l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤጇ")) in bstack1l11lll11ll_opy_ or os.environ.get(bstack1lllll1_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨገ")) in bstack1l11lll11ll_opy_
        os.environ[bstack1lllll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦጉ")] = str(bstack1l1l111l11l_opy_) # bstack1l1ll1111l1_opy_ bstack1l1ll11lll1_opy_ VAR to bstack1l1l11lllll_opy_ is binary running
        return bstack1l1l111l11l_opy_
    def bstack1l11ll11ll_opy_(self):
        for event in bstack1l1l111l1l1_opy_:
            bstack1l1ll11ll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack1l1ll11ll_opy_.logger.debug(bstack1lllll1_opy_ (u"ࠤࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠡ࠿ࡁࠤࢀࡧࡲࡨࡵࢀࠤࠧጊ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠥࠦጋ"))
            )
        bstack1l1ll11ll_opy_.register(Events.bstack1lll11l111_opy_, self.__1l1l1lllll1_opy_)
        bstack1l1ll11ll_opy_.register(Events.CONNECT, self.__1l1l11ll1l1_opy_)
        bstack1l1ll11ll_opy_.register(Events.bstack1ll11lllll_opy_, self.__1l1l111llll_opy_)
        bstack1l1ll11ll_opy_.register(Events.bstack1111l1l1ll_opy_, self.__1l1l1l1l111_opy_)
    def bstack1lllll111l_opy_(self):
        return not self.bstack1l11llll1l1_opy_ and os.environ.get(bstack1l11lll1l11_opy_, bstack1lllll1_opy_ (u"ࠦࠧጌ")) != bstack1lllll1_opy_ (u"ࠧࠨግ")
    def is_running(self):
        if self.bstack1l11llll1l1_opy_:
            return self.bstack1l1l1111lll_opy_
        else:
            return bool(self.bstack1l1l111111l_opy_)
    def bstack1l11llllll1_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1l1l1l1l11l_opy_) and cli.is_running()
    def __1l1l111ll1l_opy_(self, bstack1l1l11lll1l_opy_=10):
        if self.bstack1111111l1l_opy_:
            return
        bstack1l11llll11_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1l1l11111ll_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡛ࠣጎ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠢ࡞ࠢࡦࡳࡳࡴࡥࡤࡶ࡬ࡲ࡬ࠨጏ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1lllll1_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡣࡵࡸ࡯ࡹࡻࠥጐ"), 0), (bstack1lllll1_opy_ (u"ࠤࡪࡶࡵࡩ࠮ࡦࡰࡤࡦࡱ࡫࡟ࡩࡶࡷࡴࡸࡥࡰࡳࡱࡻࡽࠧ጑"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1l1l11lll1l_opy_)
        self.bstack1l1l111111l_opy_ = channel
        self.bstack1111111l1l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1l1l111111l_opy_)
        self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࠤጒ"), datetime.now() - bstack1l11llll11_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1l1l11111ll_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࡀࠠࡪࡵࡢࡧ࡭࡯࡬ࡥࡡࡳࡶࡴࡩࡥࡴࡵࡀࠦጓ") + str(self.bstack1lllll111l_opy_()) + bstack1lllll1_opy_ (u"ࠧࠨጔ"))
    def __1l1l111llll_opy_(self, event_name):
        if self.bstack1lllll111l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡲࡴࡵ࡯࡮ࡨࠢࡆࡐࡎࠨጕ"))
        self.__1l11lllll11_opy_()
    def __1l1l1l1l111_opy_(self, event_name, bstack1l1l11ll11l_opy_ = None, exit_code=1):
        if exit_code == 1:
            self.logger.error(bstack1lllll1_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠢ጖"))
        bstack1l1ll11ll1l_opy_ = Path(bstack1lll1lll11l_opy_ (u"ࠣࡽࡶࡩࡱ࡬࠮ࡤ࡮࡬ࡣࡩ࡯ࡲࡾ࠱ࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࡶ࠲࡯ࡹ࡯࡯ࠤ጗"))
        if self.bstack1l1l1l11lll_opy_ and bstack1l1ll11ll1l_opy_.exists():
            with open(bstack1l1ll11ll1l_opy_, bstack1lllll1_opy_ (u"ࠩࡵࠫጘ"), encoding=bstack1lllll1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩጙ")) as fp:
                data = json.load(fp)
                try:
                    bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠫࡕࡕࡓࡕࠩጚ"), bstack1lll1ll11l_opy_(bstack11l1ll1l1l_opy_), data, {
                        bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡪࠪጛ"): (self.config[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨጜ")], self.config[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪጝ")])
                    })
                except Exception as e:
                    logger.debug(bstack111llll1l_opy_.format(str(e)))
            bstack1l1ll11ll1l_opy_.unlink()
        sys.exit(exit_code)
    @measure(event_name=EVENTS.bstack1l1l11l1ll1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l1l1lllll1_opy_(self, event_name: str, data):
        from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
        self.bstack1l1l1ll1ll1_opy_, self.bstack1l1l1l11lll_opy_ = bstack1l1l1lll1l1_opy_(data.bs_config)
        os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡘࡔࡌࡘࡆࡈࡌࡆࡡࡇࡍࡗ࠭ጞ")] = self.bstack1l1l1l11lll_opy_
        if not self.bstack1l1l1ll1ll1_opy_ or not self.bstack1l1l1l11lll_opy_:
            raise ValueError(bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡈࡒࡉࠡࡤ࡬ࡲࡦࡸࡹࠣጟ"))
        if self.bstack1lllll111l_opy_():
            self.__1l1l11ll1l1_opy_(event_name, bstack1ll11l11l1_opy_())
            return
        try:
            bstack1lllllllll1_opy_.end(EVENTS.bstack111l1111ll_opy_.value, EVENTS.bstack111l1111ll_opy_.value + bstack1lllll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥጠ"), EVENTS.bstack111l1111ll_opy_.value + bstack1lllll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤጡ"), status=True, failure=None, test_name=None)
            logger.debug(bstack1lllll1_opy_ (u"ࠧࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡆࡎࠤࡘ࡫ࡴࡶࡲ࠱ࠦጢ"))
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡼࡿࠥጣ").format(e))
        start = datetime.now()
        is_started = self.__1l1l1l1111l_opy_()
        self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡴࡲࡤࡻࡳࡥࡴࡪ࡯ࡨࠦጤ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1l1l111ll1l_opy_()
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢጥ"), datetime.now() - start)
            start = datetime.now()
            self.__1l11llll1ll_opy_(data)
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢጦ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1l1l1lll11l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l1l11ll1l1_opy_(self, event_name: str, data: bstack1ll11l11l1_opy_):
        if not self.bstack1lllll111l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰࡰࡱࡩࡨࡺ࠺ࠡࡰࡲࡸࠥࡧࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢጧ"))
            return
        bin_session_id = os.environ.get(bstack1l11lll1l11_opy_)
        start = datetime.now()
        self.__1l1l111ll1l_opy_()
        self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥጨ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡃࡍࡋࠣࠦጩ") + str(bin_session_id) + bstack1lllll1_opy_ (u"ࠨࠢጪ"))
        start = datetime.now()
        self.__1l1l1ll111l_opy_()
        self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧጫ"), datetime.now() - start)
    def __1l1l1l1ll1l_opy_(self):
        if not self.bstack1111111l1l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠧጬ"))
            return
        bstack1l11ll1lll1_opy_ = {
            bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨጭ"): (bstack1ll1llll1l1_opy_, bstack1llll1l11ll_opy_, bstack1lll1l1ll11_opy_),
            bstack1lllll1_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧጮ"): (bstack1lllll1l111_opy_, bstack1lll11l111l_opy_, bstack1lllll1ll11_opy_),
        }
        if not self.bstack1l1l1l111ll_opy_ and self.session_framework in bstack1l11ll1lll1_opy_:
            bstack1l1l1l1lll1_opy_, bstack1l1l11l1lll_opy_, bstack1l1ll11ll11_opy_ = bstack1l11ll1lll1_opy_[self.session_framework]
            bstack1l1l11l1l1l_opy_ = bstack1l1l11l1lll_opy_()
            self.bstack1ll1lll1ll1_opy_ = bstack1l1l11l1l1l_opy_
            self.bstack1l1l1l111ll_opy_ = bstack1l1ll11ll11_opy_
            self.bstack1l1l1l1l11l_opy_.append(bstack1l1l11l1l1l_opy_)
            self.bstack1l1l1l1l11l_opy_.append(bstack1l1l1l1lll1_opy_(self.bstack1ll1lll1ll1_opy_))
        if not self.bstack1l1l111ll11_opy_ and self.config_observability and self.config_observability.success: # bstack1lllllll111_opy_
            self.bstack1l1l111ll11_opy_ = bstack1l1l11llll1_opy_(self.bstack1l1l1l111ll_opy_, self.bstack1ll1lll1ll1_opy_) # bstack1l1l1l1l1ll_opy_
            self.bstack1l1l1l1l11l_opy_.append(self.bstack1l1l111ll11_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1l1l1llll1l_opy_(self.bstack1l1l1l111ll_opy_, self.bstack1ll1lll1ll1_opy_)
            self.bstack1l1l1l1l11l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1lllll1_opy_ (u"ࠦࡸ࡫࡬ࡧࡊࡨࡥࡱࠨጯ"), False) == True:
            self.ai = bstack1l1ll1ll1l1_opy_()
            self.bstack1l1l1l1l11l_opy_.append(self.ai)
        if not self.percy and self.bstack1l1l1lll111_opy_ and self.bstack1l1l1lll111_opy_.success:
            self.percy = bstack1l11lll1111_opy_(self.bstack1l1l1lll111_opy_)
            self.bstack1l1l1l1l11l_opy_.append(self.percy)
        for mod in self.bstack1l1l1l1l11l_opy_:
            if not mod.bstack1lll1l11111_opy_():
                mod.configure(self.bstack1111111l1l_opy_, self.config, self.cli_bin_session_id, self.bstack1lll11lllll_opy_)
    def __1l1ll11l11l_opy_(self):
        for mod in self.bstack1l1l1l1l11l_opy_:
            if mod.bstack1lll1l11111_opy_():
                mod.configure(self.bstack1111111l1l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1l11llll11l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l11llll1ll_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1l1ll11llll_opy_:
            return
        self.__1l11llll111_opy_(data)
        bstack1l11llll11_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧጰ")
        req.sdk_language = bstack1lllll1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨጱ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1l1ll1111ll_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢ࡜ࠤጲ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢጳ"))
            r = self.bstack1111111l1l_opy_.StartBinSession(req)
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦጴ"), datetime.now() - bstack1l11llll11_opy_)
            os.environ[bstack1l11lll1l11_opy_] = r.bin_session_id
            self.__1l1l1l1ll11_opy_(r)
            self.__1l1l1l1ll1l_opy_()
            self.bstack1lll11lllll_opy_.start()
            self.bstack1l1ll11llll_opy_ = True
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥ࡟ࠧጵ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤጶ"))
        except grpc.bstack1l1l11111l1_opy_ as bstack1l1l1l1l1l1_opy_:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢጷ") + str(bstack1l1l1l1l1l1_opy_) + bstack1lllll1_opy_ (u"ࠨࠢጸ"))
            traceback.print_exc()
            raise bstack1l1l1l1l1l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጹ") + str(e) + bstack1lllll1_opy_ (u"ࠣࠤጺ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11lll1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l1l1ll111l_opy_(self):
        if not self.bstack1lllll111l_opy_() or not self.cli_bin_session_id or self.bstack1l1l1ll11l1_opy_:
            return
        bstack1l11llll11_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩጻ"), bstack1lllll1_opy_ (u"ࠪ࠴ࠬጼ")))
        try:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࠨጽ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢጾ"))
            r = self.bstack1111111l1l_opy_.ConnectBinSession(req)
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥጿ"), datetime.now() - bstack1l11llll11_opy_)
            self.__1l1l1l1ll11_opy_(r)
            self.__1l1l1l1ll1l_opy_()
            self.bstack1lll11lllll_opy_.start()
            self.bstack1l1l1ll11l1_opy_ = True
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢ࡜ࠤፀ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢፁ"))
        except grpc.bstack1l1l11111l1_opy_ as bstack1l1l1l1l1l1_opy_:
            self.logger.error(bstack1lllll1_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦፂ") + str(bstack1l1l1l1l1l1_opy_) + bstack1lllll1_opy_ (u"ࠥࠦፃ"))
            traceback.print_exc()
            raise bstack1l1l1l1l1l1_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣፄ") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨፅ"))
            traceback.print_exc()
            raise e
    def __1l1l1l1ll11_opy_(self, r):
        self.bstack1l1ll11l111_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1lllll1_opy_ (u"ࠨࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧፆ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1lllll1_opy_ (u"ࠢࡦ࡯ࡳࡸࡾࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡰࡷࡱࡨࠧፇ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1lllll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡥࡳࡥࡼࠤ࡮ࡹࠠࡴࡧࡱࡸࠥࡵ࡮࡭ࡻࠣࡥࡸࠦࡰࡢࡴࡷࠤࡴ࡬ࠠࡵࡪࡨࠤࠧࡉ࡯࡯ࡰࡨࡧࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠮ࠥࠤࡦࡴࡤࠡࡶ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡦࡲࡳࡰࠢࡸࡷࡪࡪࠠࡣࡻࠣࡗࡹࡧࡲࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡨࡶࡪ࡬࡯ࡳࡧ࠯ࠤࡓࡵ࡮ࡦࠢ࡫ࡥࡳࡪ࡬ࡪࡰࡪࠤ࡮ࡹࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥፈ")
        self.bstack1l1l1lll111_opy_ = getattr(r, bstack1lllll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨፉ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧፊ")] = self.config_testhub.jwt
        os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩፋ")] = self.config_testhub.build_hashed_id
    def bstack1l1ll111ll1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1l1l1111lll_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1l1l1111ll1_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1l1l1111ll1_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1l1ll111ll1_opy_(event_name=EVENTS.bstack1l11lll111l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l1l1l1111l_opy_(self, bstack1l1l11lll1l_opy_=10):
        if self.bstack1l1l1111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡹࡴࡢࡴࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠢፌ"))
            return True
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧፍ"))
        if os.getenv(bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡉࡓ࡜ࠢፎ")) == bstack1l1l1ll1l11_opy_:
            self.cli_bin_session_id = bstack1l1l1ll1l11_opy_
            self.cli_listen_addr = bstack1lllll1_opy_ (u"ࠣࡷࡱ࡭ࡽࡀ࠯ࡵ࡯ࡳ࠳ࡸࡪ࡫࠮ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࠩࡸ࠴ࡳࡰࡥ࡮ࠦፏ") % (self.cli_bin_session_id)
            self.bstack1l1l1111lll_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1l1l1ll1ll1_opy_, bstack1lllll1_opy_ (u"ࠤࡶࡨࡰࠨፐ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1l1l1111l1l_opy_ compat for text=True in bstack1l1l11l111l_opy_ python
            encoding=bstack1lllll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤፑ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1l11lll1ll1_opy_ = threading.Thread(target=self.__1l1l11lll11_opy_, args=(bstack1l1l11lll1l_opy_,))
        bstack1l11lll1ll1_opy_.start()
        bstack1l11lll1ll1_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡷࡵࡧࡷ࡯࠼ࠣࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࢁࠥࡵࡵࡵ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡶࡸࡩࡵࡵࡵ࠰ࡵࡩࡦࡪࠨࠪࡿࠣࡩࡷࡸ࠽ࠣፒ") + str(self.process.stderr.read()) + bstack1lllll1_opy_ (u"ࠧࠨፓ"))
        if not self.bstack1l1l1111lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡛ࠣፔ") + str(id(self)) + bstack1lllll1_opy_ (u"ࠢ࡞ࠢࡦࡰࡪࡧ࡮ࡶࡲࠥፕ"))
            self.__1l11lllll11_opy_()
        self.logger.debug(bstack1lllll1_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡱࡴࡲࡧࡪࡹࡳࡠࡴࡨࡥࡩࡿ࠺ࠡࠤፖ") + str(self.bstack1l1l1111lll_opy_) + bstack1lllll1_opy_ (u"ࠤࠥፗ"))
        return self.bstack1l1l1111lll_opy_
    def __1l1l11lll11_opy_(self, bstack1l1l1l11l1l_opy_=10):
        bstack1l1l1lll1ll_opy_ = time.time()
        while self.process and time.time() - bstack1l1l1lll1ll_opy_ < bstack1l1l1l11l1l_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1lllll1_opy_ (u"ࠥ࡭ࡩࡃࠢፘ") in line:
                    self.cli_bin_session_id = line.split(bstack1lllll1_opy_ (u"ࠦ࡮ࡪ࠽ࠣፙ"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡩ࡬ࡪࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦ࠽ࠦፚ") + str(self.cli_bin_session_id) + bstack1lllll1_opy_ (u"ࠨࠢ፛"))
                    continue
                if bstack1lllll1_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣ፜") in line:
                    self.cli_listen_addr = line.split(bstack1lllll1_opy_ (u"ࠣ࡮࡬ࡷࡹ࡫࡮࠾ࠤ፝"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡦࡰ࡮ࡥ࡬ࡪࡵࡷࡩࡳࡥࡡࡥࡦࡵ࠾ࠧ፞") + str(self.cli_listen_addr) + bstack1lllll1_opy_ (u"ࠥࠦ፟"))
                    continue
                if bstack1lllll1_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥ፠") in line:
                    port = line.split(bstack1lllll1_opy_ (u"ࠧࡶ࡯ࡳࡶࡀࠦ፡"))[-1:][0].strip()
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡰࡰࡴࡷ࠾ࠧ።") + str(port) + bstack1lllll1_opy_ (u"ࠢࠣ፣"))
                    continue
                if line.strip() == bstack1l1ll11111l_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1lllll1_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡊࡑࡢࡗ࡙ࡘࡅࡂࡏࠥ፤"), bstack1lllll1_opy_ (u"ࠤ࠴ࠦ፥")) == bstack1lllll1_opy_ (u"ࠥ࠵ࠧ፦"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1l1l1111lll_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡪࡸࡲࡰࡴ࠽ࠤࠧ፧") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨ፨"))
        return False
    @measure(event_name=EVENTS.bstack1l1l1llllll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def __1l11lllll11_opy_(self):
        if self.bstack1l1l111111l_opy_:
            self.bstack1lll11lllll_opy_.stop()
            start = datetime.now()
            if self.bstack1l11lllll1l_opy_():
                self.cli_bin_session_id = None
                if self.bstack1l1l1ll11l1_opy_:
                    self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥ፩"), datetime.now() - start)
                else:
                    self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡴࡶࡲࡴࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦ፪"), datetime.now() - start)
            self.__1l1ll11l11l_opy_()
            start = datetime.now()
            self.bstack1l1l111111l_opy_.close()
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠣࡦ࡬ࡷࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥ፫"), datetime.now() - start)
            self.bstack1l1l111111l_opy_ = None
        if self.process:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡶࡸࡴࡶࠢ፬"))
            start = datetime.now()
            self.process.terminate()
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠥ࡯࡮ࡲ࡬ࡠࡶ࡬ࡱࡪࠨ፭"), datetime.now() - start)
            self.process = None
            if self.bstack1l11llll1l1_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack11l11l1l11_opy_()
                self.logger.info(
                    bstack1lllll1_opy_ (u"࡛ࠦ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠠࡵࡱࠣࡺ࡮࡫ࡷࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡳࡳࡷࡺࠬࠡ࡫ࡱࡷ࡮࡭ࡨࡵࡵ࠯ࠤࡦࡴࡤࠡ࡯ࡤࡲࡾࠦ࡭ࡰࡴࡨࠤࡩ࡫ࡢࡶࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡧ࡬࡭ࠢࡤࡸࠥࡵ࡮ࡦࠢࡳࡰࡦࡩࡥࠢ࡞ࡱࠦ፮").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫ፯")] = self.config_testhub.build_hashed_id
        self.bstack1l1l1111lll_opy_ = False
    def __1l11llll111_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1lllll1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ፰")] = selenium.__version__
            data.frameworks.append(bstack1lllll1_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ፱"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ፲")] = __version__
            data.frameworks.append(bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ፳"))
        except:
            pass
    def bstack1l1l11l11ll_opy_(self, hub_url: str, platform_index: int, bstack1ll1ll1l11_opy_: Any):
        if self.bstack1llll1l1lll_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢ፴"))
            return
        try:
            bstack1l11llll11_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1lllll1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ፵")
            self.bstack1llll1l1lll_opy_ = bstack1lllll1ll11_opy_(
                cli.config.get(bstack1lllll1_opy_ (u"ࠧ࡮ࡵࡣࡗࡵࡰࠧ፶"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack111111111l_opy_={bstack1lllll1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥ፷"): bstack1ll1ll1l11_opy_}
            )
            def bstack1l1l11l1111_opy_(self):
                return
            if self.config.get(bstack1lllll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠤ፸"), True):
                Service.start = bstack1l1l11l1111_opy_
                Service.stop = bstack1l1l11l1111_opy_
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
            WebDriver.upload_attachment = staticmethod(bstack1l1lll1lll_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll11l11ll1_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ፹"), datetime.now() - bstack1l11llll11_opy_)
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࠣ፺") + str(e) + bstack1lllll1_opy_ (u"ࠥࠦ፻"))
    def bstack1l1l1ll11ll_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack11111l11l_opy_
            self.bstack1llll1l1lll_opy_ = bstack1lll1l1ll11_opy_(
                platform_index,
                framework_name=bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ፼"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠾ࠥࠨ፽") + str(e) + bstack1lllll1_opy_ (u"ࠨࠢ፾"))
            pass
    def bstack1l1l1l11ll1_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤ፿"))
            return
        if bstack1ll11llll1_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1lllll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᎀ"): pytest.__version__ }, [bstack1lllll1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᎁ")], self.bstack1lll11lllll_opy_, self.bstack1111111l1l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1l1l1l111l1_opy_({ bstack1lllll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᎂ"): pytest.__version__ }, [bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᎃ")], self.bstack1lll11lllll_opy_, self.bstack1111111l1l_opy_)
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࠤᎄ") + str(e) + bstack1lllll1_opy_ (u"ࠨࠢᎅ"))
        self.bstack1l1l1111111_opy_()
    def bstack1l1l1111111_opy_(self):
        if not self.bstack11ll11111_opy_():
            return
        bstack1ll11l111l_opy_ = None
        def bstack11l1llll1_opy_(config, startdir):
            return bstack1lllll1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧᎆ").format(bstack1lllll1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢᎇ"))
        def bstack1l1l1l1l1l_opy_():
            return
        def bstack1l11l111ll_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1lllll1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩᎈ"):
                return bstack1lllll1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤᎉ")
            else:
                return bstack1ll11l111l_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1ll11l111l_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack11l1llll1_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1l1l1l1l_opy_
            Config.getoption = bstack1l11l111ll_opy_
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡷࡧ࡭ࠦࡰࡺࡶࡨࡷࡹࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡨࡲࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠾ࠥࠨᎊ") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨᎋ"))
    def bstack1l1l11ll1ll_opy_(self):
        bstack1l11ll1l1l_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1l11ll1l1l_opy_, dict):
            if cli.config_observability:
                bstack1l11ll1l1l_opy_.update(
                    {bstack1lllll1_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨᎌ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1lllll1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᎍ") in accessibility.get(bstack1lllll1_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎎ"), {}):
                    bstack1l1l1ll1l1l_opy_ = accessibility.get(bstack1lllll1_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᎏ"))
                    bstack1l1l1ll1l1l_opy_.update({ bstack1lllll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠦ᎐"): bstack1l1l1ll1l1l_opy_.pop(bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢ᎑")) })
                bstack1l11ll1l1l_opy_.update({bstack1lllll1_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧ᎒"): accessibility })
        return bstack1l11ll1l1l_opy_
    @measure(event_name=EVENTS.bstack1l1ll111l11_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1l11lllll1l_opy_(self, bstack1l1l1l11111_opy_: str = None, bstack1l1l11l1l11_opy_: str = None, exit_code: int = None):
        if not self.cli_bin_session_id or not self.bstack1111111l1l_opy_:
            return
        bstack1l11llll11_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if exit_code:
            req.exit_code = exit_code
        if bstack1l1l1l11111_opy_:
            req.bstack1l1l1l11111_opy_ = bstack1l1l1l11111_opy_
        if bstack1l1l11l1l11_opy_:
            req.bstack1l1l11l1l11_opy_ = bstack1l1l11l1l11_opy_
        try:
            r = self.bstack1111111l1l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺ࡯ࡱࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢ᎓"), datetime.now() - bstack1l11llll11_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack11l1ll111_opy_(self, key: str, value: timedelta):
        tag = bstack1lllll1_opy_ (u"ࠢࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢ᎔") if self.bstack1lllll111l_opy_() else bstack1lllll1_opy_ (u"ࠣ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹࠢ᎕")
        self.bstack1l1l1l11l11_opy_[bstack1lllll1_opy_ (u"ࠤ࠽ࠦ᎖").join([tag + bstack1lllll1_opy_ (u"ࠥ࠱ࠧ᎗") + str(id(self)), key])] += value
    def bstack11l11l1l11_opy_(self):
        if not os.getenv(bstack1lllll1_opy_ (u"ࠦࡉࡋࡂࡖࡉࡢࡔࡊࡘࡆࠣ᎘"), bstack1lllll1_opy_ (u"ࠧ࠶ࠢ᎙")) == bstack1lllll1_opy_ (u"ࠨ࠱ࠣ᎚"):
            return
        bstack1l1l111lll1_opy_ = dict()
        bstack1lll1llll11_opy_ = []
        if self.test_framework:
            bstack1lll1llll11_opy_.extend(list(self.test_framework.bstack1lll1llll11_opy_.values()))
        if self.bstack1llll1l1lll_opy_:
            bstack1lll1llll11_opy_.extend(list(self.bstack1llll1l1lll_opy_.bstack1lll1llll11_opy_.values()))
        for instance in bstack1lll1llll11_opy_:
            if not instance.platform_index in bstack1l1l111lll1_opy_:
                bstack1l1l111lll1_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1l1l111lll1_opy_[instance.platform_index]
            for k, v in instance.bstack1ll1lll1111_opy_().items():
                report[k] += v
                report[k.split(bstack1lllll1_opy_ (u"ࠢ࠻ࠤ᎛"))[0]] += v
        bstack1l1l11l11l1_opy_ = sorted([(k, v) for k, v in self.bstack1l1l1l11l11_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1l1l1llll11_opy_ = 0
        for r in bstack1l1l11l11l1_opy_:
            bstack1l11lllllll_opy_ = r[1].total_seconds()
            bstack1l1l1llll11_opy_ += bstack1l11lllllll_opy_
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࢁࡲ࡜࠲ࡠࢁࡂࠨ᎜") + str(bstack1l11lllllll_opy_) + bstack1lllll1_opy_ (u"ࠤࠥ᎝"))
        self.logger.debug(bstack1lllll1_opy_ (u"ࠥ࠱࠲ࠨ᎞"))
        bstack1l11lll11l1_opy_ = []
        for platform_index, report in bstack1l1l111lll1_opy_.items():
            bstack1l11lll11l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1l11lll11l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1l1ll_opy_ = set()
        bstack1l1l1ll1111_opy_ = 0
        for r in bstack1l11lll11l1_opy_:
            bstack1l11lllllll_opy_ = r[2].total_seconds()
            bstack1l1l1ll1111_opy_ += bstack1l11lllllll_opy_
            bstack1lll1l1ll_opy_.add(r[0])
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࠱ࢀࡸ࡛࠱࡟ࢀ࠾ࢀࡸ࡛࠲࡟ࢀࡁࠧ᎟") + str(bstack1l11lllllll_opy_) + bstack1lllll1_opy_ (u"ࠧࠨᎠ"))
        if self.bstack1lllll111l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࠭࠮ࠤᎡ"))
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࢀࡺ࡯ࡵࡣ࡯ࡣࡨࡲࡩࡾࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ࠰ࡿࡸࡺࡲࠩࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠭ࢂࡃࠢᎢ") + str(bstack1l1l1ll1111_opy_) + bstack1lllll1_opy_ (u"ࠣࠤᎣ"))
        else:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࠨᎤ") + str(bstack1l1l1llll11_opy_) + bstack1lllll1_opy_ (u"ࠥࠦᎥ"))
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦ࠲࠳ࠢᎦ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str, orchestration_metadata: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files,
            orchestration_metadata=orchestration_metadata
        )
        if not self.bstack1111111l1l_opy_:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧࡩ࡬ࡪࡡࡶࡩࡷࡼࡩࡤࡧࠣ࡭ࡸࠦ࡮ࡰࡶࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࡤ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤᎧ"))
            return None
        response = self.bstack1111111l1l_opy_.TestOrchestration(request)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷ࠱ࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠱ࡸ࡫ࡳࡴ࡫ࡲࡲࡂࢁࡽࠣᎨ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1l1ll11l111_opy_(self, r):
        if r is not None and getattr(r, bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࠨᎩ"), None) and getattr(r.testhub, bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᎪ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1lllll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᎫ")))
            for bstack1l1ll111l1l_opy_, err in errors.items():
                if err[bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨᎬ")] == bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᎭ"):
                    self.logger.info(err[bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ꭾ")])
                else:
                    self.logger.error(err[bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᎯ")])
    def bstack1l111l1l1_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()