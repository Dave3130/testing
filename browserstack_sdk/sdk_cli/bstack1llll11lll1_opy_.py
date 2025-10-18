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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lll1111ll1_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_, bstack1llll1111l1_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1l1_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l1l1l1_opy_
from bstack_utils.helper import bstack1l111l11111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
import grpc
import traceback
import json
class bstack1l11llllll1_opy_(bstack1lllllllll1_opy_):
    bstack1l1ll11ll11_opy_ = False
    bstack1l1111ll1l1_opy_ = bstack11ll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᑖ")
    bstack1l1111ll11l_opy_ = bstack11ll_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᑗ")
    bstack1l111ll11l1_opy_ = bstack11ll_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡰ࡬ࡸࠧᑘ")
    bstack1l1111l1lll_opy_ = bstack11ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡶࡣࡸࡩࡡ࡯ࡰ࡬ࡲ࡬ࠨᑙ")
    bstack1l111ll11ll_opy_ = bstack11ll_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳࡡ࡫ࡥࡸࡥࡵࡳ࡮ࠥᑚ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11l1l11_opy_, bstack1ll1ll1l11l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l111l1_opy_ = False
        self.bstack1l111l111ll_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11ll11111_opy_ = bstack1ll1ll1l11l_opy_
        bstack1l1l11l1l11_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1l111l1111l_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1lll1lll1l1_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1lll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l1ll11_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        if self.bstack1l111l111l1_opy_:
            self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᑛ")] = f.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        if bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᑜ") in instance.bstack1ll111ll111_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
            self.accessibility = self.bstack1l1111l111l_opy_(tags, self.config[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᑝ")][platform_index])
        else:
            capabilities = self.bstack1l11ll11111_opy_.bstack1lll1ll1ll1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᑞ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᑟ"))
                return
            self.accessibility = self.bstack1l1111l111l_opy_(tags, capabilities)
        if self.bstack1l11ll11111_opy_.pages and self.bstack1l11ll11111_opy_.pages.values():
            bstack1l111l1ll1l_opy_ = list(self.bstack1l11ll11111_opy_.pages.values())
            if bstack1l111l1ll1l_opy_ and isinstance(bstack1l111l1ll1l_opy_[0], (list, tuple)) and bstack1l111l1ll1l_opy_[0]:
                bstack1l1111llll1_opy_ = bstack1l111l1ll1l_opy_[0][0]
                if callable(bstack1l1111llll1_opy_):
                    page = bstack1l1111llll1_opy_()
                    def bstack1l1l11l111_opy_():
                        self.get_accessibility_results(page, bstack11ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᑠ"))
                    def bstack1l1111ll111_opy_():
                        self.get_accessibility_results_summary(page, bstack11ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᑡ"))
                    setattr(page, bstack11ll_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡸࠨᑢ"), bstack1l1l11l111_opy_)
                    setattr(page, bstack11ll_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨᑣ"), bstack1l1111ll111_opy_)
        self.logger.debug(bstack11ll_opy_ (u"ࠧࡹࡨࡰࡷ࡯ࡨࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡹࡥࡱࡻࡥ࠾ࠤᑤ") + str(self.accessibility) + bstack11ll_opy_ (u"ࠨࠢᑥ"))
    def bstack1l111l1111l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l11111lll_opy_ = datetime.now()
            self.bstack1l11111ll1l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡯࡮ࡪࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥᑦ"), datetime.now() - bstack1l11111lll_opy_)
            if (
                not f.bstack1l1ll1ll11l_opy_(method_name)
                or f.bstack1l1ll1l1lll_opy_(method_name, *args)
                or f.bstack1l1ll1l1l1l_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l11llllll1_opy_.bstack1l111ll11l1_opy_, False):
                if not bstack1l11llllll1_opy_.bstack1l1ll11ll11_opy_:
                    self.logger.warning(bstack11ll_opy_ (u"ࠣ࡝ࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࠦᑧ") + str(f.platform_index) + bstack11ll_opy_ (u"ࠤࡠࠤࡦ࠷࠱ࡺࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡪࡤࡺࡪࠦ࡮ࡰࡶࠣࡦࡪ࡫࡮ࠡࡵࡨࡸࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᑨ"))
                    bstack1l11llllll1_opy_.bstack1l1ll11ll11_opy_ = True
                return
            bstack1l111ll1l11_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111ll1l11_opy_:
                platform_index = f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0)
                self.logger.debug(bstack11ll_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑩ") + str(f.framework_name) + bstack11ll_opy_ (u"ࠦࠧᑪ"))
                return
            command_name = f.bstack1l1lll11l11_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࠢᑫ") + str(method_name) + bstack11ll_opy_ (u"ࠨࠢᑬ"))
                return
            bstack1l111l1l11l_opy_ = f.get_state(instance, bstack1l11llllll1_opy_.bstack1l111ll11ll_opy_, False)
            if command_name == bstack11ll_opy_ (u"ࠢࡨࡧࡷࠦᑭ") and not bstack1l111l1l11l_opy_:
                f.bstack1llllll1lll_opy_(instance, bstack1l11llllll1_opy_.bstack1l111ll11ll_opy_, True)
                bstack1l111l1l11l_opy_ = True
            if not bstack1l111l1l11l_opy_ and not self.bstack1l111l111l1_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠣࡰࡲࠤ࡚ࡘࡌࠡ࡮ࡲࡥࡩ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑮ") + str(command_name) + bstack11ll_opy_ (u"ࠤࠥᑯ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11ll_opy_ (u"ࠥࡲࡴࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑰ") + str(command_name) + bstack11ll_opy_ (u"ࠦࠧᑱ"))
                return
            self.logger.info(bstack11ll_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻ࡭ࡧࡱࠬࡸࡩࡲࡪࡲࡷࡷࡤࡺ࡯ࡠࡴࡸࡲ࠮ࢃࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑲ") + str(command_name) + bstack11ll_opy_ (u"ࠨࠢᑳ"))
            scripts = [(s, bstack1l111ll1l11_opy_[s]) for s in scripts_to_run if s in bstack1l111ll1l11_opy_]
            for script_name, bstack1llll111lll_opy_ in scripts:
                try:
                    bstack1l11111lll_opy_ = datetime.now()
                    if script_name == bstack11ll_opy_ (u"ࠢࡴࡥࡤࡲࠧᑴ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࠢᑵ") + script_name, datetime.now() - bstack1l11111lll_opy_)
                    if isinstance(result, dict) and not result.get(bstack11ll_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵࠥᑶ"), True):
                        self.logger.warning(bstack11ll_opy_ (u"ࠥࡷࡰ࡯ࡰࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡷ࡫࡭ࡢ࡫ࡱ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺࡳ࠻ࠢࠥᑷ") + str(result) + bstack11ll_opy_ (u"ࠦࠧᑸ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11ll_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡴࡥࡵ࡭ࡵࡺ࠽ࡼࡵࡦࡶ࡮ࡶࡴࡠࡰࡤࡱࡪࢃࠠࡦࡴࡵࡳࡷࡃࠢᑹ") + str(e) + bstack11ll_opy_ (u"ࠨࠢᑺ"))
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨࠤࡪࡸࡲࡰࡴࡀࠦᑻ") + str(e) + bstack11ll_opy_ (u"ࠣࠤᑼ"))
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l1ll11_opy_(instance, args)
        capabilities = self.bstack1l11ll11111_opy_.bstack1lll1ll1ll1_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111l111l_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᑽ"))
            return
        driver = self.bstack1l11ll11111_opy_.bstack1lll1l1l1ll_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11ll1ll1_opy_)
        if not test_name:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣᑾ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        if not test_uuid:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡺࡻࡩࡥࠤᑿ"))
            return
        if isinstance(self.bstack1l11ll11111_opy_, bstack1lll1l11l1l_opy_):
            framework_name = bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒀ")
        else:
            framework_name = bstack11ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨᒁ")
        self.bstack111ll1l1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1111lll11l_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࠣᒂ"))
            return
        bstack1l11111lll_opy_ = datetime.now()
        bstack1llll111lll_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll_opy_ (u"ࠣࡵࡦࡥࡳࠨᒃ"), None)
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫࡸࡩࡡ࡯ࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒄ") + str(framework_name) + bstack11ll_opy_ (u"ࠥࠤࠧᒅ"))
            return
        if self.bstack1l111l111l1_opy_:
            arg = dict()
            arg[bstack11ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᒆ")] = method if method else bstack11ll_opy_ (u"ࠧࠨᒇ")
            arg[bstack11ll_opy_ (u"ࠨࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩࠨᒈ")] = self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᒉ")]
            arg[bstack11ll_opy_ (u"ࠣࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩࠨᒊ")] = self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠢᒋ")]
            arg[bstack11ll_opy_ (u"ࠥࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠢᒌ")] = self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠤᒍ")]
            arg[bstack11ll_opy_ (u"ࠧࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠤᒎ")] = self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᒏ")]
            arg[bstack11ll_opy_ (u"ࠢࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠢᒐ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111lll1l_opy_ = bstack1llll111lll_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111lll1l_opy_)
            return
        instance = bstack1lll1111ll1_opy_.bstack1ll11l1lll1_opy_(driver)
        if instance:
            if not bstack1lll1111ll1_opy_.get_state(instance, bstack1l11llllll1_opy_.bstack1l1111l1lll_opy_, False):
                bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, bstack1l11llllll1_opy_.bstack1l1111l1lll_opy_, True)
            else:
                self.logger.info(bstack11ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡲࠥࡶࡲࡰࡩࡵࡩࡸࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᒑ") + str(method) + bstack11ll_opy_ (u"ࠤࠥᒒ"))
                return
        self.logger.info(bstack11ll_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᒓ") + str(method) + bstack11ll_opy_ (u"ࠦࠧᒔ"))
        if framework_name == bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒕ"):
            result = self.bstack1l11ll11111_opy_.bstack1lll11l1lll_opy_(driver, bstack1llll111lll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111lll_opy_, {bstack11ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᒖ"): method if method else bstack11ll_opy_ (u"ࠢࠣᒗ")})
        bstack1llll11ll11_opy_.end(EVENTS.bstack1111lll11l_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᒘ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᒙ"), True, None, command=method)
        if instance:
            bstack1lll1111ll1_opy_.bstack1llllll1lll_opy_(instance, bstack1l11llllll1_opy_.bstack1l1111l1lll_opy_, False)
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴࠢᒚ"), datetime.now() - bstack1l11111lll_opy_)
        return result
        def bstack1l1111ll1ll_opy_(self, driver: object, framework_name, bstack11lllll1ll_opy_: str):
            self.bstack1lllll111ll_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111l1l11_opy_ = self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᒛ")]
            req.bstack11lllll1ll_opy_ = bstack11lllll1ll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllll11111_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᒜ") + str(r) + bstack11ll_opy_ (u"ࠨࠢᒝ"))
                else:
                    bstack1l111l1l1l1_opy_ = json.loads(r.bstack1l1111l1111_opy_.decode(bstack11ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᒞ")))
                    if bstack11lllll1ll_opy_ == bstack11ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬᒟ"):
                        return bstack1l111l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠤࡧࡥࡹࡧࠢᒠ"), [])
                    else:
                        return bstack1l111l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠥࡨࡦࡺࡡࠣᒡ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡰࡱࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࠢࡩࡶࡴࡳࠠࡤ࡮࡬࠾ࠥࠨᒢ") + str(e) + bstack11ll_opy_ (u"ࠧࠨᒣ"))
    @measure(event_name=EVENTS.bstack1111l11ll1_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒤ"))
            return
        if self.bstack1l111l111l1_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡡࡱࡲࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᒥ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111ll1ll_opy_(driver, framework_name, bstack11ll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒦ"))
        bstack1llll111lll_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒧ"), None)
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒨ") + str(framework_name) + bstack11ll_opy_ (u"ࠦࠧᒩ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11111lll_opy_ = datetime.now()
        if framework_name == bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒪ"):
            result = self.bstack1l11ll11111_opy_.bstack1lll11l1lll_opy_(driver, bstack1llll111lll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111lll_opy_)
        instance = bstack1lll1111ll1_opy_.bstack1ll11l1lll1_opy_(driver)
        if instance:
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࠤᒫ"), datetime.now() - bstack1l11111lll_opy_)
        return result
    @measure(event_name=EVENTS.bstack11lll1ll11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᒬ"))
            return
        if self.bstack1l111l111l1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111ll1ll_opy_(driver, framework_name, bstack11ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᒭ"))
        bstack1llll111lll_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨᒮ"), None)
        if not bstack1llll111lll_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒯ") + str(framework_name) + bstack11ll_opy_ (u"ࠦࠧᒰ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11111lll_opy_ = datetime.now()
        if framework_name == bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒱ"):
            result = self.bstack1l11ll11111_opy_.bstack1lll11l1lll_opy_(driver, bstack1llll111lll_opy_)
        else:
            result = driver.execute_async_script(bstack1llll111lll_opy_)
        instance = bstack1lll1111ll1_opy_.bstack1ll11l1lll1_opy_(driver)
        if instance:
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻࠥᒲ"), datetime.now() - bstack1l11111lll_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1111lllll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l1111l1l1l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllll11111_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᒳ") + str(r) + bstack11ll_opy_ (u"ࠣࠤᒴ"))
            else:
                self.bstack1l111l1l1ll_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᒵ") + str(e) + bstack11ll_opy_ (u"ࠥࠦᒶ"))
            traceback.print_exc()
            raise e
    def bstack1l111l1l1ll_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡱࡵࡡࡥࡡࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦᒷ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l111l1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᒸ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111l111ll_opy_[bstack11ll_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᒹ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111l111ll_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l11111ll11_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1111ll1l1_opy_ and command.module == self.bstack1l1111ll11l_opy_:
                        if command.method and not command.method in bstack1l11111ll11_opy_:
                            bstack1l11111ll11_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l11111ll11_opy_[command.method]:
                            bstack1l11111ll11_opy_[command.method][command.name] = list()
                        bstack1l11111ll11_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l11111ll11_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l11111ll1l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11ll11111_opy_, bstack1lll1l11l1l_opy_) and method_name != bstack11ll_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨᒺ"):
            return
        if bstack1lll1111ll1_opy_.bstack1lllllll111_opy_(instance, bstack1l11llllll1_opy_.bstack1l111ll11l1_opy_):
            return
        if f.bstack1lllll11ll1_opy_(method_name, *args):
            bstack1l111l11l1l_opy_ = False
            desired_capabilities = f.bstack1l1ll1l1ll1_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1ll111_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0)
                bstack1l1111l1ll1_opy_ = datetime.now()
                r = self.bstack1l1111l1l1l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᒻ"), datetime.now() - bstack1l1111l1ll1_opy_)
                bstack1l111l11l1l_opy_ = r.success
            else:
                self.logger.error(bstack11ll_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦᒼ") + str(desired_capabilities) + bstack11ll_opy_ (u"ࠥࠦᒽ"))
            f.bstack1llllll1lll_opy_(instance, bstack1l11llllll1_opy_.bstack1l111ll11l1_opy_, bstack1l111l11l1l_opy_)
    def bstack11l11lll1_opy_(self, test_tags):
        bstack1l1111l1l1l_opy_ = self.config.get(bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᒾ"))
        if not bstack1l1111l1l1l_opy_:
            return True
        try:
            include_tags = bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒿ")] if bstack11ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓀ") in bstack1l1111l1l1l_opy_ and isinstance(bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓁ")], list) else []
            exclude_tags = bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᓂ")] if bstack11ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᓃ") in bstack1l1111l1l1l_opy_ and isinstance(bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᓄ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦᓅ") + str(error))
        return False
    def bstack11ll1l1l1_opy_(self, caps):
        try:
            if self.bstack1l111l111l1_opy_:
                bstack1l111ll1111_opy_ = caps.get(bstack11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᓆ"))
                if bstack1l111ll1111_opy_ is not None and str(bstack1l111ll1111_opy_).lower() == bstack11ll_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢᓇ"):
                    bstack1l111l1l111_opy_ = caps.get(bstack11ll_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᓈ")) or caps.get(bstack11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᓉ"))
                    if bstack1l111l1l111_opy_ is not None and int(bstack1l111l1l111_opy_) < 11:
                        self.logger.warning(bstack11ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡄࡲࡩࡸ࡯ࡪࡦࠣ࠵࠶ࠦࡡ࡯ࡦࠣࡥࡧࡵࡶࡦ࠰ࠣࡇࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠ࠾ࠤᓊ") + str(bstack1l111l1l111_opy_) + bstack11ll_opy_ (u"ࠥࠦᓋ"))
                        return False
                return True
            bstack1l111l11lll_opy_ = caps.get(bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᓌ"), {}).get(bstack11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᓍ"), caps.get(bstack11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ᓎ"), bstack11ll_opy_ (u"ࠧࠨᓏ")))
            if bstack1l111l11lll_opy_:
                self.logger.warning(bstack11ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᓐ"))
                return False
            browser = caps.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᓑ"), bstack11ll_opy_ (u"ࠪࠫᓒ")).lower()
            if browser != bstack11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᓓ"):
                self.logger.warning(bstack11ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᓔ"))
                return False
            bstack1l1111lll11_opy_ = bstack1l11111llll_opy_
            if not self.config.get(bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᓕ")) or self.config.get(bstack11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᓖ")):
                bstack1l1111lll11_opy_ = bstack1l11111lll1_opy_
            browser_version = caps.get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓗ"))
            if not browser_version:
                browser_version = caps.get(bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓘ"), {}).get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᓙ"), bstack11ll_opy_ (u"ࠫࠬᓚ"))
            if browser_version and browser_version != bstack11ll_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬᓛ") and int(browser_version.split(bstack11ll_opy_ (u"࠭࠮ࠨᓜ"))[0]) <= bstack1l1111lll11_opy_:
                self.logger.warning(bstack11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࠤᓝ") + str(bstack1l1111lll11_opy_) + bstack11ll_opy_ (u"ࠣ࠰ࠥᓞ"))
                return False
            bstack1l1111l11ll_opy_ = caps.get(bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓟ"), {}).get(bstack11ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᓠ"))
            if not bstack1l1111l11ll_opy_:
                bstack1l1111l11ll_opy_ = caps.get(bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓡ"), {})
            if bstack1l1111l11ll_opy_ and bstack11ll_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩᓢ") in bstack1l1111l11ll_opy_.get(bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫᓣ"), []):
                self.logger.warning(bstack11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤᓤ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥᓥ") + str(error))
            return False
    def bstack1l111l1llll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l1111l11l1_opy_ = {
            bstack11ll_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩᓦ"): test_uuid,
        }
        bstack1l111ll111l_opy_ = {}
        if result.success:
            bstack1l111ll111l_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l11111_opy_(bstack1l1111l11l1_opy_, bstack1l111ll111l_opy_)
    def bstack111ll1l1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111l11ll_opy_ = None
        try:
            self.bstack1lllll111ll_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11ll_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥᓧ")
            req.script_name = bstack11ll_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᓨ")
            r = self.bstack1lllll11111_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡥࡴ࡬ࡺࡪࡸࠠࡦࡺࡨࡧࡺࡺࡥࠡࡲࡤࡶࡦࡳࡳࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᓩ") + str(r.error) + bstack11ll_opy_ (u"ࠨࠢᓪ"))
            else:
                bstack1l1111l11l1_opy_ = self.bstack1l111l1llll_opy_(test_uuid, r)
                bstack1llll111lll_opy_ = r.script
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪᓫ") + str(bstack1l1111l11l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll111lll_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᓬ") + str(framework_name) + bstack11ll_opy_ (u"ࠤࠣࠦᓭ"))
                return
            bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1l111l11ll1_opy_.value)
            self.bstack1l111l1lll1_opy_(driver, bstack1llll111lll_opy_, bstack1l1111l11l1_opy_, framework_name)
            self.logger.info(bstack11ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨᓮ"))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l111l11ll1_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓯ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓰ"), True, None, command=bstack11ll_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓱ"),test_name=name)
        except Exception as bstack1l111l11l11_opy_:
            self.logger.error(bstack11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤᓲ") + bstack11ll_opy_ (u"ࠣࡵࡷࡶ࠭ࡶࡡࡵࡪࠬࠦᓳ") + bstack11ll_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦᓴ") + str(bstack1l111l11l11_opy_))
            bstack1llll11ll11_opy_.end(EVENTS.bstack1l111l11ll1_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓵ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓶ"), False, bstack1l111l11l11_opy_, command=bstack11ll_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓷ"),test_name=name)
    def bstack1l111l1lll1_opy_(self, driver, bstack1llll111lll_opy_, bstack1l1111l11l1_opy_, framework_name):
        if framework_name == bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᓸ"):
            self.bstack1l11ll11111_opy_.bstack1lll11l1lll_opy_(driver, bstack1llll111lll_opy_, bstack1l1111l11l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll111lll_opy_, bstack1l1111l11l1_opy_))
    def _1l111l1ll11_opy_(self, instance: bstack1llll1111l1_opy_, args: Tuple) -> list:
        bstack11ll_opy_ (u"ࠢࠣࠤࡈࡼࡹࡸࡡࡤࡶࠣࡸࡦ࡭ࡳࠡࡤࡤࡷࡪࡪࠠࡰࡰࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࠤࠥࠦᓹ")
        if bstack11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᓺ") in instance.bstack1ll111ll111_opy_:
            return args[2].tags if hasattr(args[2], bstack11ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᓻ")) else []
        if hasattr(args[0], bstack11ll_opy_ (u"ࠪࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠨᓼ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111l111l_opy_(self, tags, capabilities):
        return self.bstack11l11lll1_opy_(tags) and self.bstack11ll1l1l1_opy_(capabilities)