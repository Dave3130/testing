# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l1ll1ll11_opy_
from browserstack_sdk.bstack11111l11_opy_ import bstack1111l1l1_opy_
def _11l1ll111l1_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l1ll1l11l_opy_:
    def __init__(self, handler):
        self._11l1ll11l1l_opy_ = {}
        self._11l1l1llll1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1111l1l1_opy_.version()
        if bstack11l1ll1ll11_opy_(pytest_version, bstack11l111_opy_ (u"ࠨ࠸࠯࠳࠱࠵ࠧᝧ")) >= 0:
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᝨ")] = Module._register_setup_function_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᝩ")] = Module._register_setup_module_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᝪ")] = Class._register_setup_class_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᝫ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠫ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᝬ"))
            Module._register_setup_module_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠬࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᝭"))
            Class._register_setup_class_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"࠭ࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᝮ"))
            Class._register_setup_method_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᝯ"))
        else:
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᝰ")] = Module._inject_setup_function_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᝱")] = Module._inject_setup_module_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᝲ")] = Class._inject_setup_class_fixture
            self._11l1ll11l1l_opy_[bstack11l111_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᝳ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᝴"))
            Module._inject_setup_module_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝵"))
            Class._inject_setup_class_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᝶"))
            Class._inject_setup_method_fixture = self.bstack11l1l1lll11_opy_(bstack11l111_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᝷"))
    def bstack11l1ll11l11_opy_(self, bstack11l1ll1l1ll_opy_, hook_type):
        bstack11l1ll1l1l1_opy_ = id(bstack11l1ll1l1ll_opy_.__class__)
        if (bstack11l1ll1l1l1_opy_, hook_type) in self._11l1l1llll1_opy_:
            return
        meth = getattr(bstack11l1ll1l1ll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1l1llll1_opy_[(bstack11l1ll1l1l1_opy_, hook_type)] = meth
            setattr(bstack11l1ll1l1ll_opy_, hook_type, self.bstack11l1ll11lll_opy_(hook_type, bstack11l1ll1l1l1_opy_))
    def bstack11l1l1lll1l_opy_(self, instance, bstack11l1ll11ll1_opy_):
        if bstack11l1ll11ll1_opy_ == bstack11l111_opy_ (u"ࠤࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠧ᝸"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠦ᝹"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠣ᝺"))
        if bstack11l1ll11ll1_opy_ == bstack11l111_opy_ (u"ࠧࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࠨ᝻"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠧ᝼"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠤ᝽"))
        if bstack11l1ll11ll1_opy_ == bstack11l111_opy_ (u"ࠣࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣ᝾"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠤࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠢ᝿"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠦក"))
        if bstack11l1ll11ll1_opy_ == bstack11l111_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠧខ"):
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠦគ"))
            self.bstack11l1ll11l11_opy_(instance.obj, bstack11l111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠣឃ"))
    @staticmethod
    def bstack11l1ll11111_opy_(hook_type, func, args):
        if hook_type in [bstack11l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ង"), bstack11l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪច")]:
            _11l1ll111l1_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1ll11lll_opy_(self, hook_type, bstack11l1ll1l1l1_opy_):
        def bstack11l1ll111ll_opy_(arg=None):
            self.handler(hook_type, bstack11l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩឆ"))
            result = None
            try:
                bstack1l11111l11l_opy_ = self._11l1l1llll1_opy_[(bstack11l1ll1l1l1_opy_, hook_type)]
                self.bstack11l1ll11111_opy_(hook_type, bstack1l11111l11l_opy_, (arg,))
                result = Result(result=bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪជ"))
            except Exception as e:
                result = Result(result=bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫឈ"), exception=e)
                self.handler(hook_type, bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫញ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬដ"), result)
        def bstack11l1l1lllll_opy_(this, arg=None):
            self.handler(hook_type, bstack11l111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧឋ"))
            result = None
            exception = None
            try:
                self.bstack11l1ll11111_opy_(hook_type, self._11l1l1llll1_opy_[hook_type], (this, arg))
                result = Result(result=bstack11l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨឌ"))
            except Exception as e:
                result = Result(result=bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩឍ"), exception=e)
                self.handler(hook_type, bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩណ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack11l111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪត"), result)
        if hook_type in [bstack11l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫថ"), bstack11l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨទ")]:
            return bstack11l1l1lllll_opy_
        return bstack11l1ll111ll_opy_
    def bstack11l1l1lll11_opy_(self, bstack11l1ll11ll1_opy_):
        def bstack11l1ll1111l_opy_(this, *args, **kwargs):
            self.bstack11l1l1lll1l_opy_(this, bstack11l1ll11ll1_opy_)
            self._11l1ll11l1l_opy_[bstack11l1ll11ll1_opy_](this, *args, **kwargs)
        return bstack11l1ll1111l_opy_