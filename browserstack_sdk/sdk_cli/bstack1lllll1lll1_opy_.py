# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1lll1111l11_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_, bstack1lll1l1l1ll_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11111ll_opy_ import bstack1lll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1lll11l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l11l_opy_ import bstack1lll11l1l11_opy_
from bstack_utils.helper import bstack1l1111ll11l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
import grpc
import traceback
import json
class bstack1l1l11l1lll_opy_(bstack1lllll111l1_opy_):
    bstack1l1ll111ll1_opy_ = False
    bstack1l111l11ll1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶࠧᑦ")
    bstack1l111l1l111_opy_ = bstack11ll1ll_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥ࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵࠦᑧ")
    bstack1l111l11111_opy_ = bstack11ll1ll_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡ࡬ࡲ࡮ࡺࠢᑨ")
    bstack1l11111ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢ࡭ࡸࡥࡳࡤࡣࡱࡲ࡮ࡴࡧࠣᑩ")
    bstack1l1111l1lll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵࡣ࡭ࡧࡳࡠࡷࡵࡰࠧᑪ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11l1l11_opy_, bstack1ll1ll11l11_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l1111l1l1l_opy_ = False
        self.bstack1l1111llll1_opy_ = dict()
        self.bstack1l111l111ll_opy_ = False
        self.bstack1l11111l11l_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l111ll1ll1_opy_ = bstack1ll1ll11l11_opy_
        bstack1l1l11l1l11_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.PRE), self.bstack1l1111l11ll_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1lll1l111l1_opy_.TEST, bstack1lll1ll1ll1_opy_.POST), self.bstack1lll1ll111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l11111l111_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_)
        if self.bstack1l1111l1l1l_opy_:
            self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᑫ")] = f.get_state(instance, TestFramework.bstack1lll11llll1_opy_)
        if bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᑬ") in instance.bstack1ll1l11111l_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1l11ll_opy_)
            self.accessibility = self.bstack1l1111lllll_opy_(tags, self.config[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᑭ")][platform_index])
        else:
            capabilities = self.bstack1l111ll1ll1_opy_.bstack1lll1lll111_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᑮ") + str(kwargs) + bstack11ll1ll_opy_ (u"ࠤࠥᑯ"))
                return
            self.accessibility = self.bstack1l1111lllll_opy_(tags, capabilities)
        if self.bstack1l111ll1ll1_opy_.pages and self.bstack1l111ll1ll1_opy_.pages.values():
            bstack1l1111l111l_opy_ = list(self.bstack1l111ll1ll1_opy_.pages.values())
            if bstack1l1111l111l_opy_ and isinstance(bstack1l1111l111l_opy_[0], (list, tuple)) and bstack1l1111l111l_opy_[0]:
                bstack1l1111l11l1_opy_ = bstack1l1111l111l_opy_[0][0]
                if callable(bstack1l1111l11l1_opy_):
                    page = bstack1l1111l11l1_opy_()
                    def bstack1l1ll11l1_opy_():
                        self.get_accessibility_results(page, bstack11ll1ll_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᑰ"))
                    def bstack1l111l1ll11_opy_():
                        self.get_accessibility_results_summary(page, bstack11ll1ll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᑱ"))
                    setattr(page, bstack11ll1ll_opy_ (u"ࠧ࡭ࡥࡵࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡓࡧࡶࡹࡱࡺࡳࠣᑲ"), bstack1l1ll11l1_opy_)
                    setattr(page, bstack11ll1ll_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡔࡷࡰࡱࡦࡸࡹࠣᑳ"), bstack1l111l1ll11_opy_)
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡴࡪࡲࡹࡱࡪࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡻࡧ࡬ࡶࡧࡀࠦᑴ") + str(self.accessibility) + bstack11ll1ll_opy_ (u"ࠣࠤᑵ"))
    def bstack1l1111l11ll_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack111111ll11_opy_ = datetime.now()
            self.bstack1l1111l1111_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡪࡰ࡬ࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᑶ"), datetime.now() - bstack111111ll11_opy_)
            if (
                not f.bstack1l1lll11ll1_opy_(method_name)
                or f.bstack1l1ll1l1lll_opy_(method_name, *args)
                or f.bstack1l1lll11l11_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l11l1lll_opy_.bstack1l111l11111_opy_, False):
                if not bstack1l1l11l1lll_opy_.bstack1l1ll111ll1_opy_:
                    self.logger.warning(bstack11ll1ll_opy_ (u"ࠥ࡟ࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨᑷ") + str(f.platform_index) + bstack11ll1ll_opy_ (u"ࠦࡢࠦࡡ࠲࠳ࡼࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣ࡬ࡦࡼࡥࠡࡰࡲࡸࠥࡨࡥࡦࡰࠣࡷࡪࡺࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡶࡩࡸࡹࡩࡰࡰࠥᑸ"))
                    bstack1l1l11l1lll_opy_.bstack1l1ll111ll1_opy_ = True
                return
            bstack1l111111l11_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111111l11_opy_:
                platform_index = f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0)
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᑹ") + str(f.framework_name) + bstack11ll1ll_opy_ (u"ࠨࠢᑺ"))
                return
            command_name = f.bstack1l1ll1lll1l_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࠤᑻ") + str(method_name) + bstack11ll1ll_opy_ (u"ࠣࠤᑼ"))
                return
            bstack1l1111ll1l1_opy_ = f.get_state(instance, bstack1l1l11l1lll_opy_.bstack1l1111l1lll_opy_, False)
            if command_name == bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࠨᑽ") and not bstack1l1111ll1l1_opy_:
                f.bstack1lllllll1l1_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l1111l1lll_opy_, True)
                bstack1l1111ll1l1_opy_ = True
            if not bstack1l1111ll1l1_opy_ and not self.bstack1l1111l1l1l_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡲࡴࠦࡕࡓࡎࠣࡰࡴࡧࡤࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᑾ") + str(command_name) + bstack11ll1ll_opy_ (u"ࠦࠧᑿ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥᒀ") + str(command_name) + bstack11ll1ll_opy_ (u"ࠨࠢᒁ"))
                return
            self.logger.info(bstack11ll1ll_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠡࡽ࡯ࡩࡳ࠮ࡳࡤࡴ࡬ࡴࡹࡹ࡟ࡵࡱࡢࡶࡺࡴࠩࡾࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᒂ") + str(command_name) + bstack11ll1ll_opy_ (u"ࠣࠤᒃ"))
            scripts = [(s, bstack1l111111l11_opy_[s]) for s in scripts_to_run if s in bstack1l111111l11_opy_]
            for script_name, bstack1lll1ll1111_opy_ in scripts:
                try:
                    bstack111111ll11_opy_ = datetime.now()
                    if script_name == bstack11ll1ll_opy_ (u"ࠤࡶࡧࡦࡴࠢᒄ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࠤᒅ") + script_name, datetime.now() - bstack111111ll11_opy_)
                    if isinstance(result, dict) and not result.get(bstack11ll1ll_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷࠧᒆ"), True):
                        self.logger.warning(bstack11ll1ll_opy_ (u"ࠧࡹ࡫ࡪࡲࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡲࡦ࡯ࡤ࡭ࡳ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵࡵ࠽ࠤࠧᒇ") + str(result) + bstack11ll1ll_opy_ (u"ࠨࠢᒈ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡶࡧࡷ࡯ࡰࡵ࠿ࡾࡷࡨࡸࡩࡱࡶࡢࡲࡦࡳࡥࡾࠢࡨࡶࡷࡵࡲ࠾ࠤᒉ") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤᒊ"))
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࠦࡥࡳࡴࡲࡶࡂࠨᒋ") + str(e) + bstack11ll1ll_opy_ (u"ࠥࠦᒌ"))
    def bstack1lll1ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l11111l111_opy_(instance, args)
        capabilities = self.bstack1l111ll1ll1_opy_.bstack1lll1lll111_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l1111lllll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒍ"))
            return
        driver = self.bstack1l111ll1ll1_opy_.bstack1lll1l1ll1l_opy_(f, instance, bstack1lllllllll1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11ll11l1_opy_)
        if not test_name:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᒎ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll11llll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᒏ"))
            return
        if isinstance(self.bstack1l111ll1ll1_opy_, bstack1lll11l11ll_opy_):
            framework_name = bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᒐ")
        else:
            framework_name = bstack11ll1ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪᒑ")
        self.bstack111ll1l1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack111l1l1l11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࠥᒒ"))
            return
        bstack111111ll11_opy_ = datetime.now()
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1ll_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᒓ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡳࡤࡣࡱࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦᒔ") + str(framework_name) + bstack11ll1ll_opy_ (u"ࠧࠦࠢᒕ"))
            return
        if self.bstack1l1111l1l1l_opy_:
            arg = dict()
            arg[bstack11ll1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᒖ")] = method if method else bstack11ll1ll_opy_ (u"ࠢࠣᒗ")
            arg[bstack11ll1ll_opy_ (u"ࠣࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠣᒘ")] = self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᒙ")]
            arg[bstack11ll1ll_opy_ (u"ࠥࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠣᒚ")] = self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᒛ")]
            arg[bstack11ll1ll_opy_ (u"ࠧࡧࡵࡵࡪࡋࡩࡦࡪࡥࡳࠤᒜ")] = self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠦᒝ")]
            arg[bstack11ll1ll_opy_ (u"ࠢࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠦᒞ")] = self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠣࡶ࡫ࡣ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠢᒟ")]
            arg[bstack11ll1ll_opy_ (u"ࠤࡶࡧࡦࡴࡔࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠤᒠ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l11111llll_opy_ = self.bstack1l111l11lll_opy_(bstack11ll1ll_opy_ (u"ࠥࡷࡨࡧ࡮ࠣᒡ"), self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᒢ")])
            if bstack11ll1ll_opy_ (u"ࠧࡩࡥ࡯ࡶࡵࡥࡱࡇࡵࡵࡪࡗࡳࡰ࡫࡮ࠣᒣ") in bstack1l11111llll_opy_:
                bstack1l11111llll_opy_ = bstack1l11111llll_opy_.copy()
                bstack1l11111llll_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡰࡷࡶࡦࡲࡁࡶࡶ࡫ࡌࡪࡧࡤࡦࡴࠥᒤ")] = bstack1l11111llll_opy_.pop(bstack11ll1ll_opy_ (u"ࠢࡤࡧࡱࡸࡷࡧ࡬ࡂࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠥᒥ"))
            arg = bstack1l1111ll11l_opy_(arg, bstack1l11111llll_opy_)
            bstack1l111l1lll1_opy_ = bstack1lll1ll1111_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l1lll1_opy_)
            return
        instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(driver)
        if instance:
            if not bstack1lll1111l11_opy_.get_state(instance, bstack1l1l11l1lll_opy_.bstack1l11111ll1l_opy_, False):
                bstack1lll1111l11_opy_.bstack1lllllll1l1_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l11111ll1l_opy_, True)
            else:
                self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡲࠥࡶࡲࡰࡩࡵࡩࡸࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡁࠧᒦ") + str(method) + bstack11ll1ll_opy_ (u"ࠤࠥᒧ"))
                return
        self.logger.info(bstack11ll1ll_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࠽ࠣᒨ") + str(method) + bstack11ll1ll_opy_ (u"ࠦࠧᒩ"))
        if framework_name == bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒪ"):
            result = self.bstack1l111ll1ll1_opy_.bstack1lll1lll1l1_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_, {bstack11ll1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᒫ"): method if method else bstack11ll1ll_opy_ (u"ࠢࠣᒬ")})
        bstack1llll11l11l_opy_.end(EVENTS.bstack111l1l1l11_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᒭ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᒮ"), True, None, command=method)
        if instance:
            bstack1lll1111l11_opy_.bstack1lllllll1l1_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l11111ll1l_opy_, False)
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻ࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴࠢᒯ"), datetime.now() - bstack111111ll11_opy_)
        return result
        def bstack1l111l1ll1l_opy_(self, driver: object, framework_name, bstack1ll11111ll_opy_: str):
            self.bstack1llllll1ll1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111l1ll1_opy_ = self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᒰ")]
            req.bstack1ll11111ll_opy_ = bstack1ll11111ll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llllll1l1l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᒱ") + str(r) + bstack11ll1ll_opy_ (u"ࠨࠢᒲ"))
                else:
                    bstack1l111111ll1_opy_ = json.loads(r.bstack1l111l1llll_opy_.decode(bstack11ll1ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᒳ")))
                    if bstack1ll11111ll_opy_ == bstack11ll1ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬᒴ"):
                        return bstack1l111111ll1_opy_.get(bstack11ll1ll_opy_ (u"ࠤࡧࡥࡹࡧࠢᒵ"), [])
                    else:
                        return bstack1l111111ll1_opy_.get(bstack11ll1ll_opy_ (u"ࠥࡨࡦࡺࡡࠣᒶ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡨࡸࡤࡧࡰࡱࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࠢࡩࡶࡴࡳࠠࡤ࡮࡬࠾ࠥࠨᒷ") + str(e) + bstack11ll1ll_opy_ (u"ࠧࠨᒸ"))
    @measure(event_name=EVENTS.bstack1111111l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒹ"))
            return
        if self.bstack1l1111l1l1l_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡡࡱࡲࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᒺ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1ll1l_opy_(driver, framework_name, bstack11ll1ll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒻ"))
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᒼ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᒽ") + str(framework_name) + bstack11ll1ll_opy_ (u"ࠦࠧᒾ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack111111ll11_opy_ = datetime.now()
        if framework_name == bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᒿ"):
            result = self.bstack1l111ll1ll1_opy_.bstack1lll1lll1l1_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_)
        instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(driver)
        if instance:
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࠤᓀ"), datetime.now() - bstack111111ll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1l111lll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷࡤࡹࡵ࡮࡯ࡤࡶࡾࡀࠠࡢ࠳࠴ࡽࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠥᓁ"))
            return
        if self.bstack1l1111l1l1l_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1ll1l_opy_(driver, framework_name, bstack11ll1ll_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᓂ"))
        bstack1lll1ll1111_opy_ = self.scripts.get(framework_name, {}).get(bstack11ll1ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨᓃ"), None)
        if not bstack1lll1ll1111_opy_:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᓄ") + str(framework_name) + bstack11ll1ll_opy_ (u"ࠦࠧᓅ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack111111ll11_opy_ = datetime.now()
        if framework_name == bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᓆ"):
            result = self.bstack1l111ll1ll1_opy_.bstack1lll1lll1l1_opy_(driver, bstack1lll1ll1111_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1ll1111_opy_)
        instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(driver)
        if instance:
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴࡡࡶࡹࡲࡳࡡࡳࡻࠥᓇ"), datetime.now() - bstack111111ll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l1l1l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l1111ll111_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llllll1l1l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᓈ") + str(r) + bstack11ll1ll_opy_ (u"ࠣࠤᓉ"))
            else:
                self.bstack1l11111l1ll_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᓊ") + str(e) + bstack11ll1ll_opy_ (u"ࠥࠦᓋ"))
            traceback.print_exc()
            raise e
    def bstack1l11111l1ll_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡱࡵࡡࡥࡡࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦᓌ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l1111l1l1l_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠥᓍ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l1111llll1_opy_[bstack11ll1ll_opy_ (u"ࠨࡴࡩࡡ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠧᓎ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l1111llll1_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l111l1_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111l11ll1_opy_ and command.module == self.bstack1l111l1l111_opy_:
                        if command.method and not command.method in bstack1l111l111l1_opy_:
                            bstack1l111l111l1_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l111l1_opy_[command.method]:
                            bstack1l111l111l1_opy_[command.method][command.name] = list()
                        bstack1l111l111l1_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l111l1_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1111l1111_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l111ll1ll1_opy_, bstack1lll11l11ll_opy_) and method_name != bstack11ll1ll_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࠨᓏ"):
            return
        if bstack1lll1111l11_opy_.bstack1lllll1llll_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l111l11111_opy_):
            return
        if f.bstack1llll1l1111_opy_(method_name, *args):
            bstack1l111111l1l_opy_ = False
            desired_capabilities = f.bstack1l1ll11llll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll111ll_opy_(instance)
                platform_index = f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0)
                bstack1l11111lll1_opy_ = datetime.now()
                r = self.bstack1l1111ll111_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᓐ"), datetime.now() - bstack1l11111lll1_opy_)
                bstack1l111111l1l_opy_ = r.success
            else:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦᓑ") + str(desired_capabilities) + bstack11ll1ll_opy_ (u"ࠥࠦᓒ"))
            f.bstack1lllllll1l1_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l111l11111_opy_, bstack1l111111l1l_opy_)
    def bstack11llll11ll_opy_(self, test_tags):
        bstack1l1111ll111_opy_ = self.config.get(bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᓓ"))
        if not bstack1l1111ll111_opy_:
            return True
        try:
            include_tags = bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᓔ")] if bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᓕ") in bstack1l1111ll111_opy_ and isinstance(bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᓖ")], list) else []
            exclude_tags = bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᓗ")] if bstack11ll1ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᓘ") in bstack1l1111ll111_opy_ and isinstance(bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᓙ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦᓚ") + str(error))
        return False
    def bstack1ll1l11ll1_opy_(self, caps):
        try:
            if self.bstack1l1111l1l1l_opy_:
                bstack1l1111lll11_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦᓛ"))
                if bstack1l1111lll11_opy_ is not None and str(bstack1l1111lll11_opy_).lower() == bstack11ll1ll_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢᓜ"):
                    bstack1l111l11l1l_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᓝ")) or caps.get(bstack11ll1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᓞ"))
                    if bstack1l111l11l1l_opy_ is not None and int(bstack1l111l11l1l_opy_) < 11:
                        self.logger.warning(bstack11ll1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡄࡲࡩࡸ࡯ࡪࡦࠣ࠵࠶ࠦࡡ࡯ࡦࠣࡥࡧࡵࡶࡦ࠰ࠣࡇࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠ࠾ࠤᓟ") + str(bstack1l111l11l1l_opy_) + bstack11ll1ll_opy_ (u"ࠥࠦᓠ"))
                        return False
                return True
            bstack1l1111ll1ll_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᓡ"), {}).get(bstack11ll1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩᓢ"), caps.get(bstack11ll1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ᓣ"), bstack11ll1ll_opy_ (u"ࠧࠨᓤ")))
            if bstack1l1111ll1ll_opy_:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧᓥ"))
                return False
            browser = caps.get(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᓦ"), bstack11ll1ll_opy_ (u"ࠪࠫᓧ")).lower()
            if browser != bstack11ll1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᓨ"):
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᓩ"))
                return False
            bstack1l11111l1l1_opy_ = bstack1l111ll1111_opy_
            if not self.config.get(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᓪ")) or self.config.get(bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᓫ")):
                bstack1l11111l1l1_opy_ = bstack1l111111lll_opy_
            browser_version = caps.get(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᓬ"))
            if not browser_version:
                browser_version = caps.get(bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓭ"), {}).get(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᓮ"), bstack11ll1ll_opy_ (u"ࠫࠬᓯ"))
            if browser_version and browser_version != bstack11ll1ll_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬᓰ") and int(browser_version.split(bstack11ll1ll_opy_ (u"࠭࠮ࠨᓱ"))[0]) <= bstack1l11111l1l1_opy_:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࠤᓲ") + str(bstack1l11111l1l1_opy_) + bstack11ll1ll_opy_ (u"ࠣ࠰ࠥᓳ"))
                return False
            bstack1l11111ll11_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᓴ"), {}).get(bstack11ll1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᓵ"))
            if not bstack1l11111ll11_opy_:
                bstack1l11111ll11_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᓶ"), {})
            if bstack1l11111ll11_opy_ and bstack11ll1ll_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩᓷ") in bstack1l11111ll11_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫᓸ"), []):
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤᓹ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥᓺ") + str(error))
            return False
    def bstack1l111l1l11l_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l1111lll1l_opy_ = {
            bstack11ll1ll_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩᓻ"): test_uuid,
        }
        bstack1l1111l1l11_opy_ = {}
        if result.success:
            bstack1l1111l1l11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111ll11l_opy_(bstack1l1111lll1l_opy_, bstack1l1111l1l11_opy_)
    def bstack1l111l11lll_opy_(self, script_name: str, test_uuid: str) -> dict:
        bstack11ll1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡇࡧࡷࡧ࡭ࠦࡣࡦࡰࡷࡶࡦࡲࠠࡢࡷࡷ࡬ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡹࡣࡳ࡫ࡳࡸࠥࡴࡡ࡮ࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡣࡢࡥ࡫ࡩࡩࠦࡣࡰࡰࡩ࡭࡬ࠦࡩࡧࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡪࡪࡺࡣࡩࡧࡧ࠰ࠥࡵࡴࡩࡧࡵࡻ࡮ࡹࡥࠡ࡮ࡲࡥࡩࡹࠠࡢࡰࡧࠤࡨࡧࡣࡩࡧࡶࠤ࡮ࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨ࠾ࠥࡔࡡ࡮ࡧࠣࡳ࡫ࠦࡴࡩࡧࠣࡷࡨࡸࡩࡱࡶࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬࡯ࡳࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡤࡻࡵࡪࡦ࠽ࠤ࡚࡛ࡉࡅࠢࡲࡪࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡹ࡫࡭ࡨ࡮ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡦࡳࡳ࡬ࡩࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡆࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾ࠲ࠠࡦ࡯ࡳࡸࡾࠦࡤࡪࡥࡷࠤ࡮࡬ࠠࡦࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᓼ")
        try:
            if self.bstack1l111l111ll_opy_:
                return self.bstack1l11111l11l_opy_
            self.bstack1llllll1ll1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11ll1ll_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᓽ")
            req.script_name = script_name
            r = self.bstack1llllll1l1l_opy_.FetchDriverExecuteParamsEvent(req)
            if r.success:
                self.bstack1l11111l11l_opy_ = self.bstack1l111l1l11l_opy_(test_uuid, r)
                self.bstack1l111l111ll_opy_ = True
            else:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠧ࡬ࡥࡵࡥ࡫ࡇࡪࡴࡴࡳࡣ࡯ࡅࡺࡺࡨࡂ࠳࠴ࡽࡈࡵ࡮ࡧ࡫ࡪ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡥࡴ࡬ࡺࡪࡸࠠࡦࡺࡨࡧࡺࡺࡥࠡࡲࡤࡶࡦࡳࡳࠡࡨࡲࡶࠥࢁࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦࠢᓾ") + str(r.error) + bstack11ll1ll_opy_ (u"ࠨࠢᓿ"))
                self.bstack1l11111l11l_opy_ = dict()
            return self.bstack1l11111l11l_opy_
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡧࡧࡷࡧ࡭ࡉࡥ࡯ࡶࡵࡥࡱࡇࡵࡵࡪࡄ࠵࠶ࡿࡃࡰࡰࡩ࡭࡬ࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡧࡶ࡮ࡼࡥࡳࠢࡨࡼࡪࡩࡵࡵࡧࠣࡴࡦࡸࡡ࡮ࡵࠣࡪࡴࡸࠠࡼࡵࡦࡶ࡮ࡶࡴࡠࡰࡤࡱࡪࢃ࠺ࠡࠤᔀ") + str(traceback.format_exc()) + bstack11ll1ll_opy_ (u"ࠣࠤᔁ"))
            return dict()
    def bstack111ll1l1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1l1lll1l1ll_opy_ = None
        try:
            self.bstack1llllll1ll1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11ll1ll_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᔂ")
            req.script_name = bstack11ll1ll_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣᔃ")
            r = self.bstack1llllll1l1l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡤࡳ࡫ࡹࡩࡷࠦࡥࡹࡧࡦࡹࡹ࡫ࠠࡱࡣࡵࡥࡲࡹࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᔄ") + str(r.error) + bstack11ll1ll_opy_ (u"ࠧࠨᔅ"))
            else:
                bstack1l1111lll1l_opy_ = self.bstack1l111l1l11l_opy_(test_uuid, r)
                bstack1lll1ll1111_opy_ = r.script
            self.logger.debug(bstack11ll1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᔆ") + str(bstack1l1111lll1l_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1ll1111_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᔇ") + str(framework_name) + bstack11ll1ll_opy_ (u"ࠣࠢࠥᔈ"))
                return
            bstack1l1lll1l1ll_opy_ = bstack1llll11l11l_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack1l111l1l1ll_opy_.value)
            self.bstack1l111l1111l_opy_(driver, bstack1lll1ll1111_opy_, bstack1l1111lll1l_opy_, framework_name)
            self.logger.info(bstack11ll1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧᔉ"))
            bstack1llll11l11l_opy_.end(EVENTS.bstack1l111l1l1ll_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᔊ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᔋ"), True, None, command=bstack11ll1ll_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᔌ"),test_name=name)
        except Exception as bstack1l111l11l11_opy_:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᔍ") + bstack11ll1ll_opy_ (u"ࠢࡴࡶࡵࠬࡵࡧࡴࡩࠫࠥᔎ") + bstack11ll1ll_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥᔏ") + str(bstack1l111l11l11_opy_))
            bstack1llll11l11l_opy_.end(EVENTS.bstack1l111l1l1ll_opy_.value, bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᔐ"), bstack1l1lll1l1ll_opy_+bstack11ll1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᔑ"), False, bstack1l111l11l11_opy_, command=bstack11ll1ll_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᔒ"),test_name=name)
    def bstack1l111l1111l_opy_(self, driver, bstack1lll1ll1111_opy_, bstack1l1111lll1l_opy_, framework_name):
        if framework_name == bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᔓ"):
            self.bstack1l111ll1ll1_opy_.bstack1lll1lll1l1_opy_(driver, bstack1lll1ll1111_opy_, bstack1l1111lll1l_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1ll1111_opy_, bstack1l1111lll1l_opy_))
    def _1l11111l111_opy_(self, instance: bstack1lll1l1l1ll_opy_, args: Tuple) -> list:
        bstack11ll1ll_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥᔔ")
        if bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᔕ") in instance.bstack1ll1l11111l_opy_:
            return args[2].tags if hasattr(args[2], bstack11ll1ll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᔖ")) else []
        if hasattr(args[0], bstack11ll1ll_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧᔗ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l1111lllll_opy_(self, tags, capabilities):
        return self.bstack11llll11ll_opy_(tags) and self.bstack1ll1l11ll1_opy_(capabilities)