# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lll1111l1l_opy_,
    bstack1lllll111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1lll111_opy_, bstack1lll1l1llll_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll11l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l1l1ll_opy_
from bstack_utils.helper import bstack1l111l111ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
import grpc
import traceback
import json
class bstack1l11lllll11_opy_(bstack1lllll1111l_opy_):
    bstack1l1ll11l1l1_opy_ = False
    bstack1l111ll1l1l_opy_ = bstack1lllll1l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨᑒ")
    bstack1l1111lll11_opy_ = bstack1lllll1l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦ࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶࠧᑓ")
    bstack1l111l1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢ࡭ࡳ࡯ࡴࠣᑔ")
    bstack1l111l111l1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡹ࡟ࡴࡥࡤࡲࡳ࡯࡮ࡨࠤᑕ")
    bstack1l111l1ll11_opy_ = bstack1lllll1l_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶࡤ࡮ࡡࡴࡡࡸࡶࡱࠨᑖ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l11ll1l1ll_opy_, bstack1ll1ll1l111_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111ll111_opy_ = False
        self.bstack1l111ll11l1_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l1111l1_opy_ = bstack1ll1ll1l111_opy_
        bstack1l11ll1l1ll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1l1111ll11l_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE), self.bstack1lll1ll1111_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111l1l11_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        if self.bstack1l1111ll111_opy_:
            self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᑗ")] = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        if bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᑘ") in instance.bstack1ll1l1l11ll_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llllllllll_opy_)
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, self.config[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᑙ")][platform_index])
        else:
            capabilities = self.bstack1l11l1111l1_opy_.bstack1lll1l111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᑚ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᑛ"))
                return
            self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if self.bstack1l11l1111l1_opy_.pages and self.bstack1l11l1111l1_opy_.pages.values():
            bstack1l1111l1ll1_opy_ = list(self.bstack1l11l1111l1_opy_.pages.values())
            if bstack1l1111l1ll1_opy_ and isinstance(bstack1l1111l1ll1_opy_[0], (list, tuple)) and bstack1l1111l1ll1_opy_[0]:
                bstack1l111l1l11l_opy_ = bstack1l1111l1ll1_opy_[0][0]
                if callable(bstack1l111l1l11l_opy_):
                    page = bstack1l111l1l11l_opy_()
                    def bstack1llll1l11l_opy_():
                        self.get_accessibility_results(page, bstack1lllll1l_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᑜ"))
                    def bstack1l111l11111_opy_():
                        self.get_accessibility_results_summary(page, bstack1lllll1l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᑝ"))
                    setattr(page, bstack1lllll1l_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡴࠤᑞ"), bstack1llll1l11l_opy_)
                    setattr(page, bstack1lllll1l_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤᑟ"), bstack1l111l11111_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡵ࡫ࡳࡺࡲࡤࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡼࡡ࡭ࡷࡨࡁࠧᑠ") + str(self.accessibility) + bstack1lllll1l_opy_ (u"ࠤࠥᑡ"))
    def bstack1l1111ll11l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1ll111ll1_opy_ = datetime.now()
            self.bstack1l1111l1l1l_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻࡫ࡱ࡭ࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᑢ"), datetime.now() - bstack1ll111ll1_opy_)
            if (
                not f.bstack1l1lll11l11_opy_(method_name)
                or f.bstack1l1ll1lll1l_opy_(method_name, *args)
                or f.bstack1l1lll111ll_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l11lllll11_opy_.bstack1l111l1ll1l_opy_, False):
                if not bstack1l11lllll11_opy_.bstack1l1ll11l1l1_opy_:
                    self.logger.warning(bstack1lllll1l_opy_ (u"ࠦࡠࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢᑣ") + str(f.platform_index) + bstack1lllll1l_opy_ (u"ࠧࡣࠠࡢ࠳࠴ࡽࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡭ࡧࡶࡦࠢࡱࡳࡹࠦࡢࡦࡧࡱࠤࡸ࡫ࡴࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡷࡪࡹࡳࡪࡱࡱࠦᑤ"))
                    bstack1l11lllll11_opy_.bstack1l1ll11l1l1_opy_ = True
                return
            bstack1l1111l111l_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111l111l_opy_:
                platform_index = f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᑥ") + str(f.framework_name) + bstack1lllll1l_opy_ (u"ࠢࠣᑦ"))
                return
            command_name = f.bstack1l1ll1ll1l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑧ") + str(method_name) + bstack1lllll1l_opy_ (u"ࠤࠥᑨ"))
                return
            bstack1l111l11l11_opy_ = f.get_state(instance, bstack1l11lllll11_opy_.bstack1l111l1ll11_opy_, False)
            if command_name == bstack1lllll1l_opy_ (u"ࠥ࡫ࡪࡺࠢᑩ") and not bstack1l111l11l11_opy_:
                f.bstack1llll11ll1l_opy_(instance, bstack1l11lllll11_opy_.bstack1l111l1ll11_opy_, True)
                bstack1l111l11l11_opy_ = True
            if not bstack1l111l11l11_opy_ and not self.bstack1l1111ll111_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡳࡵࠠࡖࡔࡏࠤࡱࡵࡡࡥࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑪ") + str(command_name) + bstack1lllll1l_opy_ (u"ࠧࠨᑫ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᑬ") + str(command_name) + bstack1lllll1l_opy_ (u"ࠢࠣᑭ"))
                return
            self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡴࡥࡵ࡭ࡵࡺࡳࡠࡶࡲࡣࡷࡻ࡮ࠪࡿࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᑮ") + str(command_name) + bstack1lllll1l_opy_ (u"ࠤࠥᑯ"))
            scripts = [(s, bstack1l1111l111l_opy_[s]) for s in scripts_to_run if s in bstack1l1111l111l_opy_]
            for script_name, bstack1lll1lll11l_opy_ in scripts:
                try:
                    bstack1ll111ll1_opy_ = datetime.now()
                    if script_name == bstack1lllll1l_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᑰ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࠥᑱ") + script_name, datetime.now() - bstack1ll111ll1_opy_)
                    if isinstance(result, dict) and not result.get(bstack1lllll1l_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨᑲ"), True):
                        self.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡳ࡬࡫ࡳࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡳࡧࡰࡥ࡮ࡴࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡶ࠾ࠥࠨᑳ") + str(result) + bstack1lllll1l_opy_ (u"ࠢࠣᑴ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡀࡿࡸࡩࡲࡪࡲࡷࡣࡳࡧ࡭ࡦࡿࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑵ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥᑶ"))
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡦࡴࡵࡳࡷࡃࠢᑷ") + str(e) + bstack1lllll1l_opy_ (u"ࠦࠧᑸ"))
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l1111l1l11_opy_(instance, args)
        capabilities = self.bstack1l11l1111l1_opy_.bstack1lll1l111ll_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111l1lll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᑹ"))
            return
        driver = self.bstack1l11l1111l1_opy_.bstack1lll1l1l111_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll111l111l_opy_)
        if not test_name:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᑺ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        if not test_uuid:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧᑻ"))
            return
        if isinstance(self.bstack1l11l1111l1_opy_, bstack1lll11l1lll_opy_):
            framework_name = bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᑼ")
        else:
            framework_name = bstack1lllll1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫᑽ")
        self.bstack1lllll11l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11111l1l11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࠦᑾ"))
            return
        bstack1ll111ll1_opy_ = datetime.now()
        bstack1lll1lll11l_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᑿ"), None)
        if not bstack1lll1lll11l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡥࡤࡲࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᒀ") + str(framework_name) + bstack1lllll1l_opy_ (u"ࠨࠠࠣᒁ"))
            return
        if self.bstack1l1111ll111_opy_:
            arg = dict()
            arg[bstack1lllll1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᒂ")] = method if method else bstack1lllll1l_opy_ (u"ࠣࠤᒃ")
            arg[bstack1lllll1l_opy_ (u"ࠤࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠤᒄ")] = self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᒅ")]
            arg[bstack1lllll1l_opy_ (u"ࠦࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠤᒆ")] = self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᒇ")]
            arg[bstack1lllll1l_opy_ (u"ࠨࡡࡶࡶ࡫ࡌࡪࡧࡤࡦࡴࠥᒈ")] = self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠧᒉ")]
            arg[bstack1lllll1l_opy_ (u"ࠣࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠧᒊ")] = self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠤࡷ࡬ࡤࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠣᒋ")]
            arg[bstack1lllll1l_opy_ (u"ࠥࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠥᒌ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l11111llll_opy_ = bstack1lll1lll11l_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l11111llll_opy_)
            return
        instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(driver)
        if instance:
            if not bstack1lll1111l1l_opy_.get_state(instance, bstack1l11lllll11_opy_.bstack1l111l111l1_opy_, False):
                bstack1lll1111l1l_opy_.bstack1llll11ll1l_opy_(instance, bstack1l11lllll11_opy_.bstack1l111l111l1_opy_, True)
            else:
                self.logger.info(bstack1lllll1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡮ࠡࡲࡵࡳ࡬ࡸࡥࡴࡵࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᒍ") + str(method) + bstack1lllll1l_opy_ (u"ࠧࠨᒎ"))
                return
        self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᒏ") + str(method) + bstack1lllll1l_opy_ (u"ࠢࠣᒐ"))
        if framework_name == bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᒑ"):
            result = self.bstack1l11l1111l1_opy_.bstack1llll11111l_opy_(driver, bstack1lll1lll11l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll11l_opy_, {bstack1lllll1l_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤᒒ"): method if method else bstack1lllll1l_opy_ (u"ࠥࠦᒓ")})
        bstack1llllllll1l_opy_.end(EVENTS.bstack11111l1l11_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᒔ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᒕ"), True, None, command=method)
        if instance:
            bstack1lll1111l1l_opy_.bstack1llll11ll1l_opy_(instance, bstack1l11lllll11_opy_.bstack1l111l111l1_opy_, False)
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰࠥᒖ"), datetime.now() - bstack1ll111ll1_opy_)
        return result
        def bstack1l111l1111l_opy_(self, driver: object, framework_name, bstack11ll11l11_opy_: str):
            self.bstack1llll1lll11_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111ll1111_opy_ = self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᒗ")]
            req.bstack11ll11l11_opy_ = bstack11ll11l11_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllllll111_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᒘ") + str(r) + bstack1lllll1l_opy_ (u"ࠤࠥᒙ"))
                else:
                    bstack1l1111lll1l_opy_ = json.loads(r.bstack1l111ll11ll_opy_.decode(bstack1lllll1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᒚ")))
                    if bstack11ll11l11_opy_ == bstack1lllll1l_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨᒛ"):
                        return bstack1l1111lll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡪࡡࡵࡣࠥᒜ"), [])
                    else:
                        return bstack1l1111lll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡤࡢࡶࡤࠦᒝ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡳࡴࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࠥ࡬ࡲࡰ࡯ࠣࡧࡱ࡯࠺ࠡࠤᒞ") + str(e) + bstack1lllll1l_opy_ (u"ࠣࠤᒟ"))
    @measure(event_name=EVENTS.bstack111ll11l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᒠ"))
            return
        if self.bstack1l1111ll111_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡤࡴࡵࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᒡ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1111l_opy_(driver, framework_name, bstack1lllll1l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣᒢ"))
        bstack1lll1lll11l_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᒣ"), None)
        if not bstack1lll1lll11l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᒤ") + str(framework_name) + bstack1lllll1l_opy_ (u"ࠢࠣᒥ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll111ll1_opy_ = datetime.now()
        if framework_name == bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᒦ"):
            result = self.bstack1l11l1111l1_opy_.bstack1llll11111l_opy_(driver, bstack1lll1lll11l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll11l_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(driver)
        if instance:
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠧᒧ"), datetime.now() - bstack1ll111ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l11lll111_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᒨ"))
            return
        if self.bstack1l1111ll111_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1111l_opy_(driver, framework_name, bstack1lllll1l_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨᒩ"))
        bstack1lll1lll11l_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤᒪ"), None)
        if not bstack1lll1lll11l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᒫ") + str(framework_name) + bstack1lllll1l_opy_ (u"ࠢࠣᒬ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll111ll1_opy_ = datetime.now()
        if framework_name == bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᒭ"):
            result = self.bstack1l11l1111l1_opy_.bstack1llll11111l_opy_(driver, bstack1lll1lll11l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1lll11l_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(driver)
        if instance:
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࠨᒮ"), datetime.now() - bstack1ll111ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1111llll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l1111ll1ll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllllll111_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᒯ") + str(r) + bstack1lllll1l_opy_ (u"ࠦࠧᒰ"))
            else:
                self.bstack1l111l11ll1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᒱ") + str(e) + bstack1lllll1l_opy_ (u"ࠨࠢᒲ"))
            traceback.print_exc()
            raise e
    def bstack1l111l11ll1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢ࡭ࡱࡤࡨࡤࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢᒳ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111ll111_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠨᒴ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111ll11l1_opy_[bstack1lllll1l_opy_ (u"ࠤࡷ࡬ࡤࡰࡷࡵࡡࡷࡳࡰ࡫࡮ࠣᒵ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111ll11l1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll111l_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111ll1l1l_opy_ and command.module == self.bstack1l1111lll11_opy_:
                        if command.method and not command.method in bstack1l111ll111l_opy_:
                            bstack1l111ll111l_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll111l_opy_[command.method]:
                            bstack1l111ll111l_opy_[command.method][command.name] = list()
                        bstack1l111ll111l_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll111l_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1111l1l1l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l1111l1_opy_, bstack1lll11l1lll_opy_) and method_name != bstack1lllll1l_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࠫᒶ"):
            return
        if bstack1lll1111l1l_opy_.bstack1lllllll11l_opy_(instance, bstack1l11lllll11_opy_.bstack1l111l1ll1l_opy_):
            return
        if f.bstack1llll1l1ll1_opy_(method_name, *args):
            bstack1l111l1llll_opy_ = False
            desired_capabilities = f.bstack1l1ll1lllll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1llll1_opy_(instance)
                platform_index = f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0)
                bstack1l1111lllll_opy_ = datetime.now()
                r = self.bstack1l1111ll1ll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡦࡳࡳ࡬ࡩࡨࠤᒷ"), datetime.now() - bstack1l1111lllll_opy_)
                bstack1l111l1llll_opy_ = r.success
            else:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡤࡦࡵ࡬ࡶࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡃࠢᒸ") + str(desired_capabilities) + bstack1lllll1l_opy_ (u"ࠨࠢᒹ"))
            f.bstack1llll11ll1l_opy_(instance, bstack1l11lllll11_opy_.bstack1l111l1ll1l_opy_, bstack1l111l1llll_opy_)
    def bstack1ll1l11ll_opy_(self, test_tags):
        bstack1l1111ll1ll_opy_ = self.config.get(bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᒺ"))
        if not bstack1l1111ll1ll_opy_:
            return True
        try:
            include_tags = bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒻ")] if bstack1lllll1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒼ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒽ")], list) else []
            exclude_tags = bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒾ")] if bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒿ") in bstack1l1111ll1ll_opy_ and isinstance(bstack1l1111ll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓀ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢᓁ") + str(error))
        return False
    def bstack1l1l1l1ll_opy_(self, caps):
        try:
            if self.bstack1l1111ll111_opy_:
                bstack1l1111l11ll_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢᓂ"))
                if bstack1l1111l11ll_opy_ is not None and str(bstack1l1111l11ll_opy_).lower() == bstack1lllll1l_opy_ (u"ࠤࡤࡲࡩࡸ࡯ࡪࡦࠥᓃ"):
                    bstack1l111l1l1l1_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠥࡥࡵࡶࡩࡶ࡯࠽ࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧᓄ")) or caps.get(bstack1lllll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᓅ"))
                    if bstack1l111l1l1l1_opy_ is not None and int(bstack1l111l1l1l1_opy_) < 11:
                        self.logger.warning(bstack1lllll1l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡇ࡮ࡥࡴࡲ࡭ࡩࠦ࠱࠲ࠢࡤࡲࡩࠦࡡࡣࡱࡹࡩ࠳ࠦࡃࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡹࡩࡷࡹࡩࡰࡰࠣࡁࠧᓆ") + str(bstack1l111l1l1l1_opy_) + bstack1lllll1l_opy_ (u"ࠨࠢᓇ"))
                        return False
                return True
            bstack1l1111l11l1_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᓈ"), {}).get(bstack1lllll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬᓉ"), caps.get(bstack1lllll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩᓊ"), bstack1lllll1l_opy_ (u"ࠪࠫᓋ")))
            if bstack1l1111l11l1_opy_:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᓌ"))
                return False
            browser = caps.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᓍ"), bstack1lllll1l_opy_ (u"࠭ࠧᓎ")).lower()
            if browser != bstack1lllll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧᓏ"):
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᓐ"))
                return False
            bstack1l111l1l1ll_opy_ = bstack1l111l11l1l_opy_
            if not self.config.get(bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᓑ")) or self.config.get(bstack1lllll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᓒ")):
                bstack1l111l1l1ll_opy_ = bstack1l1111l1111_opy_
            browser_version = caps.get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᓓ"))
            if not browser_version:
                browser_version = caps.get(bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓔ"), {}).get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᓕ"), bstack1lllll1l_opy_ (u"ࠧࠨᓖ"))
            if browser_version and browser_version != bstack1lllll1l_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨᓗ") and int(browser_version.split(bstack1lllll1l_opy_ (u"ࠩ࠱ࠫᓘ"))[0]) <= bstack1l111l1l1ll_opy_:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࠧᓙ") + str(bstack1l111l1l1ll_opy_) + bstack1lllll1l_opy_ (u"ࠦ࠳ࠨᓚ"))
                return False
            bstack1l11111ll1l_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᓛ"), {}).get(bstack1lllll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᓜ"))
            if not bstack1l11111ll1l_opy_:
                bstack1l11111ll1l_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᓝ"), {})
            if bstack1l11111ll1l_opy_ and bstack1lllll1l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬᓞ") in bstack1l11111ll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᓟ"), []):
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧᓠ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨᓡ") + str(error))
            return False
    def bstack1l1111ll1l1_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l1l111_opy_ = {
            bstack1lllll1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬᓢ"): test_uuid,
        }
        bstack1l111l11lll_opy_ = {}
        if result.success:
            bstack1l111l11lll_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l111ll_opy_(bstack1l111l1l111_opy_, bstack1l111l11lll_opy_)
    def bstack1lllll11l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111ll1l1_opy_ = None
        try:
            self.bstack1llll1lll11_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1lllll1l_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠨᓣ")
            req.script_name = bstack1lllll1l_opy_ (u"ࠢࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠧᓤ")
            r = self.bstack1lllllll111_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡨࡷ࡯ࡶࡦࡴࠣࡩࡽ࡫ࡣࡶࡶࡨࠤࡵࡧࡲࡢ࡯ࡶࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᓥ") + str(r.error) + bstack1lllll1l_opy_ (u"ࠤࠥᓦ"))
            else:
                bstack1l111l1l111_opy_ = self.bstack1l1111ll1l1_opy_(test_uuid, r)
                bstack1lll1lll11l_opy_ = r.script
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ᓧ") + str(bstack1l111l1l111_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1lll11l_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᓨ") + str(framework_name) + bstack1lllll1l_opy_ (u"ࠧࠦࠢᓩ"))
                return
            bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack1l111ll1l11_opy_.value)
            self.bstack1l11111lll1_opy_(driver, bstack1lll1lll11l_opy_, bstack1l111l1l111_opy_, framework_name)
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤᓪ"))
            bstack1llllllll1l_opy_.end(EVENTS.bstack1l111ll1l11_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᓫ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᓬ"), True, None, command=bstack1lllll1l_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᓭ"),test_name=name)
        except Exception as bstack1l111l1lll1_opy_:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧᓮ") + bstack1lllll1l_opy_ (u"ࠦࡸࡺࡲࠩࡲࡤࡸ࡭࠯ࠢᓯ") + bstack1lllll1l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢᓰ") + str(bstack1l111l1lll1_opy_))
            bstack1llllllll1l_opy_.end(EVENTS.bstack1l111ll1l11_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᓱ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᓲ"), False, bstack1l111l1lll1_opy_, command=bstack1lllll1l_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ᓳ"),test_name=name)
    def bstack1l11111lll1_opy_(self, driver, bstack1lll1lll11l_opy_, bstack1l111l1l111_opy_, framework_name):
        if framework_name == bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᓴ"):
            self.bstack1l11l1111l1_opy_.bstack1llll11111l_opy_(driver, bstack1lll1lll11l_opy_, bstack1l111l1l111_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1lll11l_opy_, bstack1l111l1l111_opy_))
    def _1l1111l1l11_opy_(self, instance: bstack1lll1l1llll_opy_, args: Tuple) -> list:
        bstack1lllll1l_opy_ (u"ࠥࠦࠧࡋࡸࡵࡴࡤࡧࡹࠦࡴࡢࡩࡶࠤࡧࡧࡳࡦࡦࠣࡳࡳࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠲ࠧࠨࠢᓵ")
        if bstack1lllll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠨᓶ") in instance.bstack1ll1l1l11ll_opy_:
            return args[2].tags if hasattr(args[2], bstack1lllll1l_opy_ (u"ࠬࡺࡡࡨࡵࠪᓷ")) else []
        if hasattr(args[0], bstack1lllll1l_opy_ (u"࠭࡯ࡸࡰࡢࡱࡦࡸ࡫ࡦࡴࡶࠫᓸ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111l1lll_opy_(self, tags, capabilities):
        return self.bstack1ll1l11ll_opy_(tags) and self.bstack1l1l1l1ll_opy_(capabilities)