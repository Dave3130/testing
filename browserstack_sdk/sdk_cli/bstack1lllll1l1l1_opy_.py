# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
    bstack1lll1111l1l_opy_,
    bstack1llll1l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_, bstack1lll1l11lll_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111lll_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll11l1ll1_opy_
from bstack_utils.helper import bstack1l111l11lll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
import grpc
import traceback
import json
class bstack1l1l1l1ll1l_opy_(bstack1lllll1l111_opy_):
    bstack1l1ll11l11l_opy_ = False
    bstack1l1111l11ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᑡ")
    bstack1l1111ll1ll_opy_ = bstack11ll1l_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧ࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨᑢ")
    bstack1l1111l11l1_opy_ = bstack11ll1l_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡴࡩࡵࠤᑣ")
    bstack1l111l1l1ll_opy_ = bstack11ll1l_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯ࡳࡠࡵࡦࡥࡳࡴࡩ࡯ࡩࠥᑤ")
    bstack1l11111l1ll_opy_ = bstack11ll1l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡥࡨࡢࡵࡢࡹࡷࡲࠢᑥ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1ll1l11_opy_, bstack1ll1ll1llll_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l1l1l1_opy_ = False
        self.bstack1l1111l1111_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l11ll1l_opy_ = bstack1ll1ll1llll_opy_
        bstack1l1l1ll1l11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_, bstack1llll11l1l1_opy_.PRE), self.bstack1l1111ll111_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack1lllll111ll_opy_((bstack1lll1l1l11l_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11ll1_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        if self.bstack1l111l1l1l1_opy_:
            self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠢᑦ")] = f.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        if bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᑧ") in instance.bstack1ll111l11l1_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1lllll1llll_opy_)
            self.accessibility = self.bstack1l1111ll11l_opy_(tags, self.config[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᑨ")][platform_index])
        else:
            capabilities = self.bstack1l11l11ll1l_opy_.bstack1lll11l11ll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᑩ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠦࠧᑪ"))
                return
            self.accessibility = self.bstack1l1111ll11l_opy_(tags, capabilities)
        if self.bstack1l11l11ll1l_opy_.pages and self.bstack1l11l11ll1l_opy_.pages.values():
            bstack1l1111l1l11_opy_ = list(self.bstack1l11l11ll1l_opy_.pages.values())
            if bstack1l1111l1l11_opy_ and isinstance(bstack1l1111l1l11_opy_[0], (list, tuple)) and bstack1l1111l1l11_opy_[0]:
                bstack1l1111l1lll_opy_ = bstack1l1111l1l11_opy_[0][0]
                if callable(bstack1l1111l1lll_opy_):
                    page = bstack1l1111l1lll_opy_()
                    def bstack11l11l1l1l_opy_():
                        self.get_accessibility_results(page, bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤᑫ"))
                    def bstack1l111l111l1_opy_():
                        self.get_accessibility_results_summary(page, bstack11ll1l_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᑬ"))
                    setattr(page, bstack11ll1l_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡵࠥᑭ"), bstack11l11l1l1l_opy_)
                    setattr(page, bstack11ll1l_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡖࡹࡲࡳࡡࡳࡻࠥᑮ"), bstack1l111l111l1_opy_)
        self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡶ࡬ࡴࡻ࡬ࡥࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡶࡢ࡮ࡸࡩࡂࠨᑯ") + str(self.accessibility) + bstack11ll1l_opy_ (u"ࠥࠦᑰ"))
    def bstack1l1111ll111_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1ll11ll111_opy_ = datetime.now()
            self.bstack1l111l11111_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼࡬ࡲ࡮ࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡤࡱࡱࡪ࡮࡭ࠢᑱ"), datetime.now() - bstack1ll11ll111_opy_)
            if (
                not f.bstack1l1ll1lll1l_opy_(method_name)
                or f.bstack1l1ll1lll11_opy_(method_name, *args)
                or f.bstack1l1ll1l1l11_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l1l1ll1l_opy_.bstack1l1111l11l1_opy_, False):
                if not bstack1l1l1l1ll1l_opy_.bstack1l1ll11l11l_opy_:
                    self.logger.warning(bstack11ll1l_opy_ (u"ࠧࡡࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࠣᑲ") + str(f.platform_index) + bstack11ll1l_opy_ (u"ࠨ࡝ࠡࡣ࠴࠵ࡾࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡮ࡡࡷࡧࠣࡲࡴࡺࠠࡣࡧࡨࡲࠥࡹࡥࡵࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᑳ"))
                    bstack1l1l1l1ll1l_opy_.bstack1l1ll11l11l_opy_ = True
                return
            bstack1l111l1lll1_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111l1lll1_opy_:
                platform_index = f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0)
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡯ࡱࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᑴ") + str(f.framework_name) + bstack11ll1l_opy_ (u"ࠣࠤᑵ"))
                return
            command_name = f.bstack1l1ll1l1ll1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࠦᑶ") + str(method_name) + bstack11ll1l_opy_ (u"ࠥࠦᑷ"))
                return
            bstack1l11111l1l1_opy_ = f.get_state(instance, bstack1l1l1l1ll1l_opy_.bstack1l11111l1ll_opy_, False)
            if command_name == bstack11ll1l_opy_ (u"ࠦ࡬࡫ࡴࠣᑸ") and not bstack1l11111l1l1_opy_:
                f.bstack1llll1l1lll_opy_(instance, bstack1l1l1l1ll1l_opy_.bstack1l11111l1ll_opy_, True)
                bstack1l11111l1l1_opy_ = True
            if not bstack1l11111l1l1_opy_ and not self.bstack1l111l1l1l1_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡴ࡯ࠡࡗࡕࡐࠥࡲ࡯ࡢࡦࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᑹ") + str(command_name) + bstack11ll1l_opy_ (u"ࠨࠢᑺ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡯ࡱࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑻ") + str(command_name) + bstack11ll1l_opy_ (u"ࠣࠤᑼ"))
                return
            self.logger.info(bstack11ll1l_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠣࡿࡱ࡫࡮ࠩࡵࡦࡶ࡮ࡶࡴࡴࡡࡷࡳࡤࡸࡵ࡯ࠫࢀࠤࡸࡩࡲࡪࡲࡷࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦᑽ") + str(command_name) + bstack11ll1l_opy_ (u"ࠥࠦᑾ"))
            scripts = [(s, bstack1l111l1lll1_opy_[s]) for s in scripts_to_run if s in bstack1l111l1lll1_opy_]
            for script_name, bstack1lll11l1l1l_opy_ in scripts:
                try:
                    bstack1ll11ll111_opy_ = datetime.now()
                    if script_name == bstack11ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᑿ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽ࠦᒀ") + script_name, datetime.now() - bstack1ll11ll111_opy_)
                    if isinstance(result, dict) and not result.get(bstack11ll1l_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹࠢᒁ"), True):
                        self.logger.warning(bstack11ll1l_opy_ (u"ࠢࡴ࡭࡬ࡴࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡴࡨࡱࡦ࡯࡮ࡪࡰࡪࠤࡸࡩࡲࡪࡲࡷࡷ࠿ࠦࠢᒂ") + str(result) + bstack11ll1l_opy_ (u"ࠣࠤᒃ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11ll1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡸࡩࡲࡪࡲࡷࡁࢀࡹࡣࡳ࡫ࡳࡸࡤࡴࡡ࡮ࡧࢀࠤࡪࡸࡲࡰࡴࡀࠦᒄ") + str(e) + bstack11ll1l_opy_ (u"ࠥࠦᒅ"))
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡧࡵࡶࡴࡸ࠽ࠣᒆ") + str(e) + bstack11ll1l_opy_ (u"ࠧࠨᒇ"))
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11ll1_opy_(instance, args)
        capabilities = self.bstack1l11l11ll1l_opy_.bstack1lll11l11ll_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111ll11l_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᒈ"))
            return
        driver = self.bstack1l11l11ll1l_opy_.bstack1lll1lll111_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11111l1l_opy_)
        if not test_name:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡯ࡣࡰࡩࠧᒉ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡷࡸ࡭ࡩࠨᒊ"))
            return
        if isinstance(self.bstack1l11l11ll1l_opy_, bstack1lll1llllll_opy_):
            framework_name = bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᒋ")
        else:
            framework_name = bstack11ll1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬᒌ")
        self.bstack1lll111ll_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack1ll1111lll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࠧᒍ"))
            return
        bstack1ll11ll111_opy_ = datetime.now()
        bstack1lll11l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1l_opy_ (u"ࠧࡹࡣࡢࡰࠥᒎ"), None)
        if not bstack1lll11l1l1l_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡦࡥࡳ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᒏ") + str(framework_name) + bstack11ll1l_opy_ (u"ࠢࠡࠤᒐ"))
            return
        if self.bstack1l111l1l1l1_opy_:
            arg = dict()
            arg[bstack11ll1l_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣᒑ")] = method if method else bstack11ll1l_opy_ (u"ࠤࠥᒒ")
            arg[bstack11ll1l_opy_ (u"ࠥࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠥᒓ")] = self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᒔ")]
            arg[bstack11ll1l_opy_ (u"ࠧࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠥᒕ")] = self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠦᒖ")]
            arg[bstack11ll1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠦᒗ")] = self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳࠨᒘ")]
            arg[bstack11ll1l_opy_ (u"ࠤࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳࠨᒙ")] = self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠥࡸ࡭ࡥࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠤᒚ")]
            arg[bstack11ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠦᒛ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111l1l1l_opy_ = bstack1lll11l1l1l_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111l1l1l_opy_)
            return
        instance = bstack1lll1111l1l_opy_.bstack1ll111l1l11_opy_(driver)
        if instance:
            if not bstack1lll1111l1l_opy_.get_state(instance, bstack1l1l1l1ll1l_opy_.bstack1l111l1l1ll_opy_, False):
                bstack1lll1111l1l_opy_.bstack1llll1l1lll_opy_(instance, bstack1l1l1l1ll1l_opy_.bstack1l111l1l1ll_opy_, True)
            else:
                self.logger.info(bstack11ll1l_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡯ࠢࡳࡶࡴ࡭ࡲࡦࡵࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤᒜ") + str(method) + bstack11ll1l_opy_ (u"ࠨࠢᒝ"))
                return
        self.logger.info(bstack11ll1l_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᒞ") + str(method) + bstack11ll1l_opy_ (u"ࠣࠤᒟ"))
        if framework_name == bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᒠ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1lll11l1l11_opy_(driver, bstack1lll11l1l1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11l1l1l_opy_, {bstack11ll1l_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᒡ"): method if method else bstack11ll1l_opy_ (u"ࠦࠧᒢ")})
        bstack1llll111ll1_opy_.end(EVENTS.bstack1ll1111lll_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᒣ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᒤ"), True, None, command=method)
        if instance:
            bstack1lll1111l1l_opy_.bstack1llll1l1lll_opy_(instance, bstack1l1l1l1ll1l_opy_.bstack1l111l1l1ll_opy_, False)
            instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱࠦᒥ"), datetime.now() - bstack1ll11ll111_opy_)
        return result
        def bstack1l1111llll1_opy_(self, driver: object, framework_name, bstack11lllll1ll_opy_: str):
            self.bstack1llll1l11l1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111l111ll_opy_ = self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᒦ")]
            req.bstack11lllll1ll_opy_ = bstack11lllll1ll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllll111l1_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᒧ") + str(r) + bstack11ll1l_opy_ (u"ࠥࠦᒨ"))
                else:
                    bstack1l1111l1ll1_opy_ = json.loads(r.bstack1l1111lll11_opy_.decode(bstack11ll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᒩ")))
                    if bstack11lllll1ll_opy_ == bstack11ll1l_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᒪ"):
                        return bstack1l1111l1ll1_opy_.get(bstack11ll1l_opy_ (u"ࠨࡤࡢࡶࡤࠦᒫ"), [])
                    else:
                        return bstack1l1111l1ll1_opy_.get(bstack11ll1l_opy_ (u"ࠢࡥࡣࡷࡥࠧᒬ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11ll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡴࡵࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࠦࡦࡳࡱࡰࠤࡨࡲࡩ࠻ࠢࠥᒭ") + str(e) + bstack11ll1l_opy_ (u"ࠤࠥᒮ"))
    @measure(event_name=EVENTS.bstack1111l111ll_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᒯ"))
            return
        if self.bstack1l111l1l1l1_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡥࡵࡶࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᒰ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111llll1_opy_(driver, framework_name, bstack11ll1l_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠤᒱ"))
        bstack1lll11l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥᒲ"), None)
        if not bstack1lll11l1l1l_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᒳ") + str(framework_name) + bstack11ll1l_opy_ (u"ࠣࠤᒴ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll11ll111_opy_ = datetime.now()
        if framework_name == bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᒵ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1lll11l1l11_opy_(driver, bstack1lll11l1l1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11l1l1l_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1ll111l1l11_opy_(driver)
        if instance:
            instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࠨᒶ"), datetime.now() - bstack1ll11ll111_opy_)
        return result
    @measure(event_name=EVENTS.bstack11ll1l111_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒷ"))
            return
        if self.bstack1l111l1l1l1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111llll1_opy_(driver, framework_name, bstack11ll1l_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩᒸ"))
        bstack1lll11l1l1l_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1l_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠥᒹ"), None)
        if not bstack1lll11l1l1l_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᒺ") + str(framework_name) + bstack11ll1l_opy_ (u"ࠣࠤᒻ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1ll11ll111_opy_ = datetime.now()
        if framework_name == bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᒼ"):
            result = self.bstack1l11l11ll1l_opy_.bstack1lll11l1l11_opy_(driver, bstack1lll11l1l1l_opy_)
        else:
            result = driver.execute_async_script(bstack1lll11l1l1l_opy_)
        instance = bstack1lll1111l1l_opy_.bstack1ll111l1l11_opy_(driver)
        if instance:
            instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿࠢᒽ"), datetime.now() - bstack1ll11ll111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1111lll1l_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1l111l1ll1l_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1l11l1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllll111l1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᒾ") + str(r) + bstack11ll1l_opy_ (u"ࠧࠨᒿ"))
            else:
                self.bstack1l1111l111l_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᓀ") + str(e) + bstack11ll1l_opy_ (u"ࠢࠣᓁ"))
            traceback.print_exc()
            raise e
    def bstack1l1111l111l_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣ࡮ࡲࡥࡩࡥࡣࡰࡰࡩ࡭࡬ࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣᓂ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l1l1l1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠢᓃ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111l1111_opy_[bstack11ll1l_opy_ (u"ࠥࡸ࡭ࡥࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠤᓄ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111l1111_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l1llll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1111l11ll_opy_ and command.module == self.bstack1l1111ll1ll_opy_:
                        if command.method and not command.method in bstack1l111l1llll_opy_:
                            bstack1l111l1llll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l1llll_opy_[command.method]:
                            bstack1l111l1llll_opy_[command.method][command.name] = list()
                        bstack1l111l1llll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l1llll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l11111_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l11ll1l_opy_, bstack1lll1llllll_opy_) and method_name != bstack11ll1l_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࠬᓅ"):
            return
        if bstack1lll1111l1l_opy_.bstack1llllllll11_opy_(instance, bstack1l1l1l1ll1l_opy_.bstack1l1111l11l1_opy_):
            return
        if f.bstack1lllll1ll11_opy_(method_name, *args):
            bstack1l111l11l1l_opy_ = False
            desired_capabilities = f.bstack1l1lll111ll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1ll1ll11l_opy_(instance)
                platform_index = f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0)
                bstack1l111l1l111_opy_ = datetime.now()
                r = self.bstack1l111l1ll1l_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡧࡴࡴࡦࡪࡩࠥᓆ"), datetime.now() - bstack1l111l1l111_opy_)
                bstack1l111l11l1l_opy_ = r.success
            else:
                self.logger.error(bstack11ll1l_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡥࡧࡶ࡭ࡷ࡫ࡤࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠽ࠣᓇ") + str(desired_capabilities) + bstack11ll1l_opy_ (u"ࠢࠣᓈ"))
            f.bstack1llll1l1lll_opy_(instance, bstack1l1l1l1ll1l_opy_.bstack1l1111l11l1_opy_, bstack1l111l11l1l_opy_)
    def bstack111l1ll11_opy_(self, test_tags):
        bstack1l111l1ll1l_opy_ = self.config.get(bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨᓉ"))
        if not bstack1l111l1ll1l_opy_:
            return True
        try:
            include_tags = bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᓊ")] if bstack11ll1l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᓋ") in bstack1l111l1ll1l_opy_ and isinstance(bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᓌ")], list) else []
            exclude_tags = bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᓍ")] if bstack11ll1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓎ") in bstack1l111l1ll1l_opy_ and isinstance(bstack1l111l1ll1l_opy_[bstack11ll1l_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓏ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡶࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨࡧ࡮࡯࡫ࡱ࡫࠳ࠦࡅࡳࡴࡲࡶࠥࡀࠠࠣᓐ") + str(error))
        return False
    def bstack1111l11l1_opy_(self, caps):
        try:
            if self.bstack1l111l1l1l1_opy_:
                bstack1l1111lllll_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᓑ"))
                if bstack1l1111lllll_opy_ is not None and str(bstack1l1111lllll_opy_).lower() == bstack11ll1l_opy_ (u"ࠥࡥࡳࡪࡲࡰ࡫ࡧࠦᓒ"):
                    bstack1l111l11l11_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠦࡦࡶࡰࡪࡷࡰ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᓓ")) or caps.get(bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᓔ"))
                    if bstack1l111l11l11_opy_ is not None and int(bstack1l111l11l11_opy_) < 11:
                        self.logger.warning(bstack11ll1l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡁ࡯ࡦࡵࡳ࡮ࡪࠠ࠲࠳ࠣࡥࡳࡪࠠࡢࡤࡲࡺࡪ࠴ࠠࡄࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡺࡪࡸࡳࡪࡱࡱࠤࡂࠨᓕ") + str(bstack1l111l11l11_opy_) + bstack11ll1l_opy_ (u"ࠢࠣᓖ"))
                        return False
                return True
            bstack1l11111llll_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᓗ"), {}).get(bstack11ll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ᓘ"), caps.get(bstack11ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪᓙ"), bstack11ll1l_opy_ (u"ࠫࠬᓚ")))
            if bstack1l11111llll_opy_:
                self.logger.warning(bstack11ll1l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡊࡥࡴ࡭ࡷࡳࡵࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤᓛ"))
                return False
            browser = caps.get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᓜ"), bstack11ll1l_opy_ (u"ࠧࠨᓝ")).lower()
            if browser != bstack11ll1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨᓞ"):
                self.logger.warning(bstack11ll1l_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᓟ"))
                return False
            bstack1l11111ll1l_opy_ = bstack1l111l1111l_opy_
            if not self.config.get(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᓠ")) or self.config.get(bstack11ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᓡ")):
                bstack1l11111ll1l_opy_ = bstack1l111ll111l_opy_
            browser_version = caps.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᓢ"))
            if not browser_version:
                browser_version = caps.get(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᓣ"), {}).get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᓤ"), bstack11ll1l_opy_ (u"ࠨࠩᓥ"))
            if browser_version and browser_version != bstack11ll1l_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩᓦ") and int(browser_version.split(bstack11ll1l_opy_ (u"ࠪ࠲ࠬᓧ"))[0]) <= bstack1l11111ll1l_opy_:
                self.logger.warning(bstack11ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࠨᓨ") + str(bstack1l11111ll1l_opy_) + bstack11ll1l_opy_ (u"ࠧ࠴ࠢᓩ"))
                return False
            bstack1l111l1l11l_opy_ = caps.get(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᓪ"), {}).get(bstack11ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᓫ"))
            if not bstack1l111l1l11l_opy_:
                bstack1l111l1l11l_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᓬ"), {})
            if bstack1l111l1l11l_opy_ and bstack11ll1l_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭ᓭ") in bstack1l111l1l11l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨᓮ"), []):
                self.logger.warning(bstack11ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨᓯ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻࡧ࡬ࡪࡦࡤࡸࡪࠦࡡ࠲࠳ࡼࠤࡸࡻࡰࡱࡱࡵࡸࠥࡀࠢᓰ") + str(error))
            return False
    def bstack1l11111ll11_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l11111lll1_opy_ = {
            bstack11ll1l_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ᓱ"): test_uuid,
        }
        bstack1l111ll1111_opy_ = {}
        if result.success:
            bstack1l111ll1111_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l111l11lll_opy_(bstack1l11111lll1_opy_, bstack1l111ll1111_opy_)
    def bstack1lll111ll_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll111l1l1l_opy_ = None
        try:
            self.bstack1llll1l11l1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11ll1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢᓲ")
            req.script_name = bstack11ll1l_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨᓳ")
            r = self.bstack1lllll111l1_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤࡩࡸࡩࡷࡧࡵࠤࡪࡾࡥࡤࡷࡷࡩࠥࡶࡡࡳࡣࡰࡷࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᓴ") + str(r.error) + bstack11ll1l_opy_ (u"ࠥࠦᓵ"))
            else:
                bstack1l11111lll1_opy_ = self.bstack1l11111ll11_opy_(test_uuid, r)
                bstack1lll11l1l1l_opy_ = r.script
            self.logger.debug(bstack11ll1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧᓶ") + str(bstack1l11111lll1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll11l1l1l_opy_:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᓷ") + str(framework_name) + bstack11ll1l_opy_ (u"ࠨࠠࠣᓸ"))
                return
            bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack1l111l1ll11_opy_.value)
            self.bstack1l1111ll1l1_opy_(driver, bstack1lll11l1l1l_opy_, bstack1l11111lll1_opy_, framework_name)
            self.logger.info(bstack11ll1l_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥᓹ"))
            bstack1llll111ll1_opy_.end(EVENTS.bstack1l111l1ll11_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᓺ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᓻ"), True, None, command=bstack11ll1l_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨᓼ"),test_name=name)
        except Exception as bstack1l11111l11l_opy_:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨᓽ") + bstack11ll1l_opy_ (u"ࠧࡹࡴࡳࠪࡳࡥࡹ࡮ࠩࠣᓾ") + bstack11ll1l_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣᓿ") + str(bstack1l11111l11l_opy_))
            bstack1llll111ll1_opy_.end(EVENTS.bstack1l111l1ll11_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔀ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔁ"), False, bstack1l11111l11l_opy_, command=bstack11ll1l_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᔂ"),test_name=name)
    def bstack1l1111ll1l1_opy_(self, driver, bstack1lll11l1l1l_opy_, bstack1l11111lll1_opy_, framework_name):
        if framework_name == bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᔃ"):
            self.bstack1l11l11ll1l_opy_.bstack1lll11l1l11_opy_(driver, bstack1lll11l1l1l_opy_, bstack1l11111lll1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll11l1l1l_opy_, bstack1l11111lll1_opy_))
    def _1l111l11ll1_opy_(self, instance: bstack1lll1l11lll_opy_, args: Tuple) -> list:
        bstack11ll1l_opy_ (u"ࠦࠧࠨࡅࡹࡶࡵࡥࡨࡺࠠࡵࡣࡪࡷࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࠨࠢࠣᔄ")
        if bstack11ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᔅ") in instance.bstack1ll111l11l1_opy_:
            return args[2].tags if hasattr(args[2], bstack11ll1l_opy_ (u"࠭ࡴࡢࡩࡶࠫᔆ")) else []
        if hasattr(args[0], bstack11ll1l_opy_ (u"ࠧࡰࡹࡱࡣࡲࡧࡲ࡬ࡧࡵࡷࠬᔇ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111ll11l_opy_(self, tags, capabilities):
        return self.bstack111l1ll11_opy_(tags) and self.bstack1111l11l1_opy_(capabilities)